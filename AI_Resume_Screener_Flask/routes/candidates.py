"""
routes/candidates.py — Upload, list, detail, status update
"""

import json, os, uuid
from flask import (Blueprint, render_template, request, redirect,
                   url_for, session, flash, send_file)
from database.db import get_db
from utils.ai_pipeline import analyse_resume
from utils.report_generator import generate_csv, generate_text_report
import io

candidates_bp = Blueprint("candidates", __name__)

ALLOWED = {".pdf", ".docx"}
UPLOAD_FOLDER = "uploads"


def login_required(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapper


def _safe_json(val):
    """Parse a JSON string, return [] on failure."""
    if not val:
        return []
    try:
        return json.loads(val)
    except Exception:
        return []


# ── Upload ────────────────────────────────────────────────────────────────────

@candidates_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    conn = get_db()
    jobs = conn.execute("SELECT id, title, department FROM jobs WHERE status='active'").fetchall()
    conn.close()

    if request.method == "GET":
        return render_template("upload.html", jobs=jobs)

    # POST — process uploaded files
    files  = request.files.getlist("resumes")
    job_id = request.form.get("job_id") or None

    if not files or all(f.filename == "" for f in files):
        flash("Please select at least one resume file.", "warning")
        return redirect(url_for("candidates.upload"))

    # Fetch job details for matching
    job = None
    if job_id:
        conn = get_db()
        row = conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        conn.close()
        if row:
            job = {
                "required_skills": _safe_json(row["required_skills"]),
                "jd_text": row["jd_text"] or "",
                "min_experience": row["min_experience"] or 0,
            }

    results = []
    conn = get_db()
    for upload_file in files:
        if not upload_file.filename:
            continue
        ext = os.path.splitext(upload_file.filename)[1].lower()
        if ext not in ALLOWED:
            results.append({"name": upload_file.filename, "error": "Unsupported file type"})
            continue

        file_bytes = upload_file.read()
        if len(file_bytes) > 10 * 1024 * 1024:
            results.append({"name": upload_file.filename, "error": "File too large (>10MB)"})
            continue

        # Save file to disk
        safe_name = f"{uuid.uuid4().hex}{ext}"
        save_path = os.path.join(UPLOAD_FOLDER, safe_name)
        with open(save_path, "wb") as f:
            f.write(file_bytes)

        # Run AI pipeline
        data = analyse_resume(file_bytes, upload_file.filename, job)
        data["resume_filename"] = safe_name

        # Insert into database
        conn.execute("""
            INSERT INTO candidates
            (job_id, name, email, phone, linkedin, github, portfolio,
             years_experience, education, technical_skills, soft_skills, certifications,
             ats_score, skill_match, experience_match, education_match,
             semantic_score, keyword_score, overall_score,
             matched_skills, missing_skills, recommended_skills,
             recommendation, recommendation_label,
             ai_summary, ai_insights, raw_text, resume_filename,
             status)
            VALUES
            (:job_id, :name, :email, :phone, :linkedin, :github, :portfolio,
             :years_experience, :education, :technical_skills, :soft_skills, :certifications,
             :ats_score, :skill_match, :experience_match, :education_match,
             :semantic_score, :keyword_score, :overall_score,
             :matched_skills, :missing_skills, :recommended_skills,
             :recommendation, :recommendation_label,
             :ai_summary, :ai_insights, :raw_text, :resume_filename,
             'new')
        """, {**data, "job_id": job_id})

        results.append({
            "name": data["name"],
            "score": data["ats_score"],
            "label": data["recommendation_label"],
            "error": None,
        })

    conn.commit()
    conn.close()

    flash(f"✅ {len([r for r in results if not r.get('error')])} resume(s) analysed successfully!", "success")
    return render_template("upload_results.html", results=results)


# ── Candidate List ────────────────────────────────────────────────────────────

@candidates_bp.route("/candidates")
@login_required
def list_candidates():
    search     = request.args.get("search", "").strip()
    reco       = request.args.get("recommendation", "")
    min_score  = request.args.get("min_score", "")
    job_filter = request.args.get("job_id", "")
    page       = int(request.args.get("page", 1))
    per_page   = 20

    conn = get_db()
    query  = "SELECT * FROM candidates WHERE 1=1"
    params = []
    if search:
        query += " AND name LIKE ?"
        params.append(f"%{search}%")
    if reco:
        query += " AND recommendation = ?"
        params.append(reco)
    if min_score:
        query += " AND ats_score >= ?"
        params.append(float(min_score))
    if job_filter:
        query += " AND job_id = ?"
        params.append(int(job_filter))

    total      = conn.execute(f"SELECT COUNT(*) FROM ({query})", params).fetchone()[0]
    query     += f" ORDER BY ats_score DESC LIMIT {per_page} OFFSET {(page-1)*per_page}"
    candidates = [dict(c) for c in conn.execute(query, params).fetchall()]
    jobs       = conn.execute("SELECT id, title FROM jobs").fetchall()
    conn.close()

    # Parse JSON fields for display
    for c in candidates:
        c["tech_skills_list"] = _safe_json(c["technical_skills"])[:5]
        c["education_list"]   = _safe_json(c["education"])

    total_pages = (total + per_page - 1) // per_page

    return render_template(
        "candidates.html",
        candidates=candidates, total=total,
        page=page, total_pages=total_pages,
        search=search, reco=reco,
        min_score=min_score, job_filter=job_filter,
        jobs=jobs,
    )


# ── Candidate Detail ──────────────────────────────────────────────────────────

@candidates_bp.route("/candidates/<int:cid>")
@login_required
def detail(cid):
    conn = get_db()
    c = conn.execute("SELECT * FROM candidates WHERE id=?", (cid,)).fetchone()
    conn.close()
    if not c:
        flash("Candidate not found.", "danger")
        return redirect(url_for("candidates.list_candidates"))

    c = dict(c)
    c["tech_skills_list"]  = _safe_json(c["technical_skills"])
    c["soft_skills_list"]  = _safe_json(c["soft_skills"])
    c["education_list"]    = _safe_json(c["education"])
    c["certs_list"]        = _safe_json(c["certifications"])
    c["matched_list"]      = _safe_json(c["matched_skills"])
    c["missing_list"]      = _safe_json(c["missing_skills"])
    c["reco_list"]         = _safe_json(c["recommended_skills"])
    c["insights_list"]     = _safe_json(c["ai_insights"])

    return render_template("candidate_detail.html", c=c)


# ── Status Update ─────────────────────────────────────────────────────────────

@candidates_bp.route("/candidates/<int:cid>/status", methods=["POST"])
@login_required
def update_status(cid):
    status = request.form.get("status", "new")
    conn = get_db()
    conn.execute("UPDATE candidates SET status=? WHERE id=?", (status, cid))
    conn.commit()
    conn.close()
    flash(f"Status updated to '{status}'.", "success")
    return redirect(url_for("candidates.detail", cid=cid))


# ── Delete ────────────────────────────────────────────────────────────────────

@candidates_bp.route("/candidates/<int:cid>/delete", methods=["POST"])
@login_required
def delete(cid):
    conn = get_db()
    row = conn.execute("SELECT resume_filename FROM candidates WHERE id=?", (cid,)).fetchone()
    if row and row["resume_filename"]:
        path = os.path.join(UPLOAD_FOLDER, row["resume_filename"])
        if os.path.exists(path):
            os.remove(path)
    conn.execute("DELETE FROM candidates WHERE id=?", (cid,))
    conn.commit()
    conn.close()
    flash("Candidate deleted.", "info")
    return redirect(url_for("candidates.list_candidates"))


# ── Export CSV ────────────────────────────────────────────────────────────────

@candidates_bp.route("/candidates/export/csv")
@login_required
def export_csv():
    conn = get_db()
    candidates = [dict(c) for c in conn.execute(
        "SELECT * FROM candidates ORDER BY ats_score DESC"
    ).fetchall()]
    conn.close()

    csv_bytes = generate_csv(candidates)
    return send_file(
        io.BytesIO(csv_bytes),
        mimetype="text/csv",
        as_attachment=True,
        download_name="candidates_report.csv",
    )


# ── Export Single Text Report ─────────────────────────────────────────────────

@candidates_bp.route("/candidates/<int:cid>/report")
@login_required
def export_report(cid):
    conn = get_db()
    c = conn.execute("SELECT * FROM candidates WHERE id=?", (cid,)).fetchone()
    conn.close()
    if not c:
        flash("Candidate not found.", "danger")
        return redirect(url_for("candidates.list_candidates"))

    report_text = generate_text_report(dict(c))
    return send_file(
        io.BytesIO(report_text.encode("utf-8")),
        mimetype="text/plain",
        as_attachment=True,
        download_name=f"{dict(c)['name'].replace(' ','_')}_report.txt",
    )
