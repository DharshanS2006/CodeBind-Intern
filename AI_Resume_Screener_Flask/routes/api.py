"""
routes/api.py — JSON API endpoints consumed by Chart.js on the frontend
"""

import json
from collections import Counter
from flask import Blueprint, jsonify, session
from database.db import get_db

api_bp = Blueprint("api", __name__, url_prefix="/api")


def _safe_json(val):
    if not val:
        return []
    try:
        return json.loads(val)
    except Exception:
        return []


@api_bp.route("/stats")
def stats():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_db()
    candidates = conn.execute("SELECT * FROM candidates").fetchall()
    conn.close()

    total       = len(candidates)
    shortlisted = sum(1 for c in candidates if c["recommendation"] == "shortlist")
    rejected    = sum(1 for c in candidates if c["recommendation"] == "reject")
    avg_score   = round(sum(c["ats_score"] for c in candidates) / total, 1) if total else 0

    bands = {"90-100": 0, "70-89": 0, "50-69": 0, "30-49": 0, "0-29": 0}
    for c in candidates:
        s = c["ats_score"] or 0
        if s >= 90:   bands["90-100"] += 1
        elif s >= 70: bands["70-89"]  += 1
        elif s >= 50: bands["50-69"]  += 1
        elif s >= 30: bands["30-49"]  += 1
        else:         bands["0-29"]   += 1

    skill_freq = Counter()
    for c in candidates:
        skill_freq.update(_safe_json(c["technical_skills"]))

    return jsonify({
        "total": total,
        "shortlisted": shortlisted,
        "rejected": rejected,
        "avg_score": avg_score,
        "score_bands": bands,
        "top_skills": dict(skill_freq.most_common(10)),
    })
