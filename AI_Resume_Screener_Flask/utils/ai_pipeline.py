"""
utils/ai_pipeline.py
Orchestrates the full AI analysis pipeline:
  parse → extract skills → score → recommend → summarise
"""

import json
from utils.resume_parser import parse_resume
from utils.skill_extractor import (
    extract_technical_skills, extract_soft_skills,
    get_matched_skills, get_missing_skills, get_recommended_skills,
)
from utils.resume_matcher import (
    semantic_similarity, keyword_score, skill_match_score,
    experience_match_score, education_match_score, communication_score,
    compute_ats_score, get_recommendation, generate_insights, generate_summary,
)


def analyse_resume(file_bytes: bytes, filename: str, job: dict = None) -> dict:
    """
    Run the complete AI pipeline on one resume.

    Parameters:
        file_bytes  : raw bytes of the uploaded file
        filename    : original filename (used for type detection)
        job         : dict with keys required_skills, jd_text, min_experience

    Returns a flat dict ready to INSERT into the candidates table.
    """
    # ── Step 1: Parse ──────────────────────────────────────────────────────
    parsed = parse_resume(file_bytes, filename)
    raw_text    = parsed["raw_text"]
    name        = parsed["name"]
    email       = parsed["email"]
    phone       = parsed["phone"]
    linkedin    = parsed["linkedin"]
    github      = parsed["github"]
    portfolio   = parsed["portfolio"]
    years_exp   = parsed["years_experience"]
    education   = parsed["education"]
    certs       = parsed["certifications"]

    # ── Step 2: Skills ─────────────────────────────────────────────────────
    tech_skills  = extract_technical_skills(raw_text)
    soft_skills  = extract_soft_skills(raw_text)

    # ── Step 3: Job-specific matching ──────────────────────────────────────
    required_skills = (job.get("required_skills") or []) if job else []
    jd_text         = (job.get("jd_text") or "") if job else ""
    min_exp         = int((job.get("min_experience") or 0)) if job else 0

    matched  = get_matched_skills(tech_skills, required_skills)
    missing  = get_missing_skills(tech_skills, required_skills)
    reco_skills = get_recommended_skills(missing)

    # ── Step 4: Scoring ────────────────────────────────────────────────────
    s_skill  = skill_match_score(tech_skills, required_skills)
    s_exp    = experience_match_score(years_exp, min_exp)
    s_edu    = education_match_score(education)
    s_sem    = semantic_similarity(raw_text, jd_text) if jd_text else 70.0
    s_kw     = keyword_score(raw_text, jd_text)     if jd_text else 65.0
    s_comm   = communication_score(raw_text)

    ats = compute_ats_score(s_skill, s_exp, s_edu, s_sem, s_kw, len(certs))
    rec_status, rec_label = get_recommendation(ats)

    # ── Step 5: AI output ──────────────────────────────────────────────────
    insights = generate_insights(tech_skills, missing, years_exp, ats)
    summary  = generate_summary(name, years_exp, tech_skills, missing, ats, rec_label)

    return {
        "name": name, "email": email, "phone": phone,
        "linkedin": linkedin, "github": github, "portfolio": portfolio,
        "years_experience": years_exp,
        "education": json.dumps(education),
        "technical_skills": json.dumps(tech_skills),
        "soft_skills": json.dumps(soft_skills),
        "certifications": json.dumps(certs),
        "ats_score": ats,
        "skill_match": s_skill,
        "experience_match": s_exp,
        "education_match": s_edu,
        "semantic_score": s_sem,
        "keyword_score": s_kw,
        "overall_score": ats,
        "matched_skills": json.dumps(matched),
        "missing_skills": json.dumps(missing),
        "recommended_skills": json.dumps(reco_skills),
        "recommendation": rec_status,
        "recommendation_label": rec_label,
        "ai_summary": summary,
        "ai_insights": json.dumps(insights),
        "raw_text": raw_text[:8000],   # Limit stored text size
        "resume_filename": filename,
    }
