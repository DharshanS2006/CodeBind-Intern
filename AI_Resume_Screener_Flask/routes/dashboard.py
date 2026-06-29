"""
routes/dashboard.py — Main dashboard page
"""

import json
from flask import Blueprint, render_template, session, redirect, url_for
from database.db import get_db

dashboard_bp = Blueprint("dashboard", __name__)


def login_required(f):
    """Simple decorator that redirects to login if not authenticated."""
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapper


@dashboard_bp.route("/dashboard")
@login_required
def index():
    conn = get_db()
    candidates = conn.execute(
        "SELECT * FROM candidates ORDER BY ats_score DESC"
    ).fetchall()
    jobs = conn.execute("SELECT * FROM jobs").fetchall()
    conn.close()

    total       = len(candidates)
    shortlisted = sum(1 for c in candidates if c["recommendation"] == "shortlist")
    rejected    = sum(1 for c in candidates if c["recommendation"] == "reject")
    maybe       = sum(1 for c in candidates if c["recommendation"] == "maybe")
    avg_score   = round(
        sum(c["ats_score"] for c in candidates) / total, 1
    ) if total else 0
    top = dict(candidates[0]) if candidates else None

    # Score distribution for Chart.js
    bands = {"90-100": 0, "70-89": 0, "50-69": 0, "30-49": 0, "0-29": 0}
    for c in candidates:
        s = c["ats_score"] or 0
        if s >= 90:   bands["90-100"] += 1
        elif s >= 70: bands["70-89"]  += 1
        elif s >= 50: bands["50-69"]  += 1
        elif s >= 30: bands["30-49"]  += 1
        else:         bands["0-29"]   += 1

    # Monthly uploads
    monthly = {}
    for c in candidates:
        if c["created_at"]:
            month = c["created_at"][:7]   # "2025-03"
            monthly[month] = monthly.get(month, 0) + 1
    monthly_labels  = list(monthly.keys())[-6:]
    monthly_data    = [monthly[m] for m in monthly_labels]

    # Skill frequency
    skill_freq = {}
    for c in candidates:
        try:
            for s in json.loads(c["technical_skills"] or "[]"):
                skill_freq[s] = skill_freq.get(s, 0) + 1
        except Exception:
            pass
    top_skills = sorted(skill_freq.items(), key=lambda x: -x[1])[:8]

    # Recommendation breakdown
    reco_breakdown = {
        "Highly Recommended": sum(1 for c in candidates if c["recommendation_label"] == "Highly Recommended"),
        "Recommended":        sum(1 for c in candidates if c["recommendation_label"] == "Recommended"),
        "Needs Review":       sum(1 for c in candidates if c["recommendation_label"] == "Needs Review"),
        "Not Recommended":    sum(1 for c in candidates if c["recommendation_label"] == "Not Recommended"),
    }

    recent = [dict(c) for c in candidates[:5]]

    return render_template(
        "dashboard.html",
        total=total, shortlisted=shortlisted, rejected=rejected,
        maybe=maybe, avg_score=avg_score, top=top,
        bands=json.dumps(bands),
        monthly_labels=json.dumps(monthly_labels),
        monthly_data=json.dumps(monthly_data),
        top_skills=json.dumps(dict(top_skills)),
        reco_breakdown=json.dumps(reco_breakdown),
        recent=recent, jobs=jobs,
        active_jobs=sum(1 for j in jobs if j["status"] == "active"),
    )
