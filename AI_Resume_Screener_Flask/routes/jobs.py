"""
routes/jobs.py — Job openings CRUD
"""

import json
from flask import (Blueprint, render_template, request,
                   redirect, url_for, session, flash)
from database.db import get_db

jobs_bp = Blueprint("jobs", __name__)


def login_required(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapper


@jobs_bp.route("/jobs")
@login_required
def list_jobs():
    conn = get_db()
    jobs = conn.execute("""
        SELECT j.*, COUNT(c.id) as candidate_count
        FROM jobs j
        LEFT JOIN candidates c ON c.job_id = j.id
        GROUP BY j.id ORDER BY j.created_at DESC
    """).fetchall()
    conn.close()
    return render_template("jobs.html", jobs=[dict(j) for j in jobs])


@jobs_bp.route("/jobs/new", methods=["GET", "POST"])
@login_required
def new_job():
    if request.method == "POST":
        title      = request.form.get("title", "").strip()
        dept       = request.form.get("department", "").strip()
        location   = request.form.get("location", "").strip()
        jd_text    = request.form.get("jd_text", "").strip()
        skills_raw = request.form.get("required_skills", "").strip()
        min_exp    = int(request.form.get("min_experience", 0))

        skills = [s.strip().lower() for s in skills_raw.split(",") if s.strip()]

        conn = get_db()
        conn.execute("""
            INSERT INTO jobs (title, department, location, jd_text, required_skills, min_experience)
            VALUES (?,?,?,?,?,?)
        """, (title, dept, location, jd_text, json.dumps(skills), min_exp))
        conn.commit()
        conn.close()
        flash(f"Job '{title}' created!", "success")
        return redirect(url_for("jobs.list_jobs"))

    return render_template("job_form.html", job=None)


@jobs_bp.route("/jobs/<int:jid>/edit", methods=["GET", "POST"])
@login_required
def edit_job(jid):
    conn = get_db()
    job = conn.execute("SELECT * FROM jobs WHERE id=?", (jid,)).fetchone()
    if not job:
        conn.close()
        flash("Job not found.", "danger")
        return redirect(url_for("jobs.list_jobs"))

    if request.method == "POST":
        title      = request.form.get("title", "").strip()
        dept       = request.form.get("department", "").strip()
        location   = request.form.get("location", "").strip()
        jd_text    = request.form.get("jd_text", "").strip()
        skills_raw = request.form.get("required_skills", "").strip()
        min_exp    = int(request.form.get("min_experience", 0))
        status     = request.form.get("status", "active")

        skills = [s.strip().lower() for s in skills_raw.split(",") if s.strip()]

        conn.execute("""
            UPDATE jobs SET title=?,department=?,location=?,jd_text=?,
            required_skills=?,min_experience=?,status=? WHERE id=?
        """, (title, dept, location, jd_text, json.dumps(skills), min_exp, status, jid))
        conn.commit()
        conn.close()
        flash("Job updated.", "success")
        return redirect(url_for("jobs.list_jobs"))

    job = dict(job)
    try:
        job["skills_str"] = ", ".join(json.loads(job["required_skills"] or "[]"))
    except Exception:
        job["skills_str"] = ""
    conn.close()
    return render_template("job_form.html", job=job)


@jobs_bp.route("/jobs/<int:jid>/delete", methods=["POST"])
@login_required
def delete_job(jid):
    conn = get_db()
    conn.execute("DELETE FROM jobs WHERE id=?", (jid,))
    conn.commit()
    conn.close()
    flash("Job deleted.", "info")
    return redirect(url_for("jobs.list_jobs"))
