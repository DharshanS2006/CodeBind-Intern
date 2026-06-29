"""
utils/report_generator.py
Generates downloadable CSV and simple text reports.
"""

import csv
import io
import json
from datetime import datetime


def generate_csv(candidates: list) -> bytes:
    """
    Generate a CSV report from a list of candidate row dicts.
    Returns bytes suitable for Flask send_file.
    """
    output = io.StringIO()
    writer = csv.writer(output)

    # Header row
    writer.writerow([
        "Rank", "Name", "Email", "Phone",
        "Years Experience", "ATS Score", "Skill Match %",
        "Experience Match %", "Education Match %", "Semantic Score %",
        "Recommendation", "Status",
        "Matched Skills", "Missing Skills", "Education",
    ])

    for i, c in enumerate(candidates, 1):
        # Parse JSON fields safely
        def safe_json(val):
            if not val:
                return ""
            try:
                return ", ".join(json.loads(val))
            except Exception:
                return str(val)

        writer.writerow([
            i,
            c["name"] or "",
            c["email"] or "",
            c["phone"] or "",
            f"{c['years_experience']:.1f}",
            f"{c['ats_score']:.1f}",
            f"{c['skill_match']:.1f}",
            f"{c['experience_match']:.1f}",
            f"{c['education_match']:.1f}",
            f"{c['semantic_score']:.1f}",
            c["recommendation_label"] or "",
            c["status"] or "",
            safe_json(c["matched_skills"]),
            safe_json(c["missing_skills"]),
            safe_json(c["education"]),
        ])

    output.seek(0)
    return output.getvalue().encode("utf-8")


def generate_text_report(candidate: dict) -> str:
    """
    Generate a plain-text single-candidate report.
    """
    def safe_json(val):
        if not val:
            return "None"
        try:
            items = json.loads(val)
            return ", ".join(items) if items else "None"
        except Exception:
            return str(val)

    lines = [
        "=" * 60,
        "  AI RESUME SCREENING SYSTEM — CANDIDATE REPORT",
        "=" * 60,
        f"  Generated: {datetime.now().strftime('%B %d, %Y %H:%M')}",
        "",
        "CANDIDATE INFORMATION",
        "-" * 40,
        f"  Name         : {candidate['name']}",
        f"  Email        : {candidate['email'] or '—'}",
        f"  Phone        : {candidate['phone'] or '—'}",
        f"  LinkedIn     : {candidate['linkedin'] or '—'}",
        f"  GitHub       : {candidate['github'] or '—'}",
        f"  Experience   : {candidate['years_experience']:.1f} years",
        f"  Education    : {safe_json(candidate['education'])}",
        "",
        "AI SCORING BREAKDOWN",
        "-" * 40,
        f"  ATS Score         : {candidate['ats_score']:.1f} / 100",
        f"  Skill Match       : {candidate['skill_match']:.1f}%",
        f"  Experience Match  : {candidate['experience_match']:.1f}%",
        f"  Education Match   : {candidate['education_match']:.1f}%",
        f"  Semantic Score    : {candidate['semantic_score']:.1f}%",
        "",
        "RECOMMENDATION",
        "-" * 40,
        f"  {candidate['recommendation_label']}",
        "",
        "AI SUMMARY",
        "-" * 40,
        f"  {candidate['ai_summary'] or '—'}",
        "",
        "SKILLS",
        "-" * 40,
        f"  Matched  : {safe_json(candidate['matched_skills'])}",
        f"  Missing  : {safe_json(candidate['missing_skills'])}",
        "",
        "=" * 60,
        "  Powered by TalentScan AI Resume Screener",
        "=" * 60,
    ]
    return "\n".join(lines)
