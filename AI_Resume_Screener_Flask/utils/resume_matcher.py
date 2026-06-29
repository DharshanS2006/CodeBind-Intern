"""
utils/resume_matcher.py
AI Matching Engine — TF-IDF Cosine Similarity + Weighted ATS Scoring.

For a college project this demonstrates:
- TF-IDF vectorisation (scikit-learn)
- Cosine similarity (semantic matching)
- Skill overlap scoring
- Weighted composite ATS score
"""

import math
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ── TF-IDF Semantic Similarity ───────────────────────────────────────────────

def semantic_similarity(text1: str, text2: str) -> float:
    """
    Compute cosine similarity between two text documents using TF-IDF.
    Uses unigrams + bigrams for better phrase matching.
    Returns a score from 0–100.
    """
    if not text1.strip() or not text2.strip():
        return 0.0
    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),      # captures "machine learning", "rest api"
            max_features=5000,
            sublinear_tf=True,       # dampen effect of very frequent terms
        )
        matrix = vectorizer.fit_transform([text1, text2])
        score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        return round(float(score) * 100, 1)
    except Exception:
        return 0.0


# ── Keyword Matching Score ────────────────────────────────────────────────────

def keyword_score(resume_text: str, jd_text: str) -> float:
    """
    Count how many JD keywords appear in the resume.
    Returns a score from 0–100.
    """
    if not jd_text.strip():
        return 50.0
    # Tokenize JD into meaningful words (3+ chars, alphabetic)
    jd_words = set(re.findall(r'\b[a-z]{3,}\b', jd_text.lower()))
    resume_words = set(re.findall(r'\b[a-z]{3,}\b', resume_text.lower()))
    if not jd_words:
        return 0.0
    overlap = jd_words & resume_words
    return round((len(overlap) / len(jd_words)) * 100, 1)


# ── Skill Match Score ─────────────────────────────────────────────────────────

def skill_match_score(resume_skills: list, required_skills: list) -> float:
    """
    Percentage of JD-required skills found in the resume.
    Returns 0–100.
    """
    if not required_skills:
        return 75.0  # If no skills specified, give neutral score
    resume_set = {s.lower() for s in resume_skills}
    matches = sum(1 for s in required_skills if s.lower() in resume_set)
    return round((matches / len(required_skills)) * 100, 1)


# ── Experience Match Score ────────────────────────────────────────────────────

def experience_match_score(years: float, min_required: int = 0) -> float:
    """
    Score how well the candidate's experience meets the minimum required.
    Returns 0–100.
    """
    if min_required == 0:
        # No requirement: give a generous score scaled by years
        return min(100.0, 50 + years * 6)
    ratio = years / max(min_required, 1)
    return round(min(100.0, ratio * 85), 1)


# ── Education Match Score ─────────────────────────────────────────────────────

DEGREE_WEIGHT = {
    "phd": 1.0, "m.tech": 0.9, "m.sc": 0.85, "mba": 0.85,
    "b.tech": 0.75, "b.sc": 0.7, "bca": 0.65, "mca": 0.85, "diploma": 0.55,
}

def education_match_score(education: list) -> float:
    """
    Score the candidate's education level.
    Returns 0–100.
    """
    if not education:
        return 50.0
    best = max(
        (DEGREE_WEIGHT.get(e.lower(), 0.5) for e in education),
        default=0.5
    )
    return round(best * 100, 1)


# ── Communication Score ───────────────────────────────────────────────────────

ACTION_VERBS = [
    "led", "managed", "delivered", "achieved", "designed", "built",
    "implemented", "collaborated", "mentored", "reduced", "increased",
    "optimised", "launched", "developed", "created", "improved",
]

def communication_score(resume_text: str) -> float:
    """
    Heuristic score based on action verbs and professional language.
    Returns 0–100.
    """
    text_lower = resume_text.lower()
    hits = sum(1 for verb in ACTION_VERBS if verb in text_lower)
    return round(min(100, 45 + hits * 4), 1)


# ── ATS Composite Score ───────────────────────────────────────────────────────

def compute_ats_score(
    skill_score: float,
    exp_score: float,
    edu_score: float,
    sem_score: float,
    kw_score: float,
    cert_count: int,
) -> float:
    """
    Weighted ATS composite score.

    Weights:
        Skill Match       → 35%
        Experience Match  → 25%
        Education Match   → 15%
        Semantic Match    → 15%
        Keyword Match     → 10%
        Certification Bonus (up to +8 pts)
    """
    cert_bonus = min(8, cert_count * 2.5)
    raw = (
        skill_score   * 0.35 +
        exp_score     * 0.25 +
        edu_score     * 0.15 +
        sem_score     * 0.15 +
        kw_score      * 0.10 +
        cert_bonus
    )
    return round(min(99.0, max(8.0, raw)), 1)


# ── Recommendation ────────────────────────────────────────────────────────────

def get_recommendation(score: float) -> tuple:
    """
    Map ATS score to a human-readable recommendation.
    Returns (status, label).
    """
    if score >= 80:
        return ("shortlist", "Highly Recommended")
    elif score >= 65:
        return ("shortlist", "Recommended")
    elif score >= 45:
        return ("maybe", "Needs Review")
    else:
        return ("reject", "Not Recommended")


# ── AI Insights ───────────────────────────────────────────────────────────────

def generate_insights(
    skills: list, missing: list, years: float, score: float
) -> list:
    """Generate short recruiter-friendly insight strings."""
    insights = []
    backend_skills  = {"python", "fastapi", "django", "flask", "node.js", "java", "spring"}
    ml_skills       = {"pytorch", "tensorflow", "scikit-learn", "machine learning", "deep learning"}
    cloud_skills    = {"aws", "azure", "gcp", "kubernetes", "docker"}
    skill_set       = set(skills)

    if backend_skills & skill_set:
        insights.append("Strong backend engineering profile")
    if ml_skills & skill_set:
        insights.append("Solid ML / AI skill set")
    if cloud_skills & skill_set:
        insights.append("Cloud-native experience present")
    if "docker" in missing:
        insights.append("Lacks containerisation experience (Docker)")
    if "kubernetes" in missing:
        insights.append("No orchestration experience (Kubernetes)")
    if years >= 5:
        insights.append("Senior-level experience — high value candidate")
    elif years <= 1:
        insights.append("Early-career candidate — high growth potential")
    if score >= 80:
        insights.append("Excellent overall ATS match")
    elif score < 45:
        insights.append("Significant skill gaps relative to this role")
    return insights[:5]


# ── Summary Generator ─────────────────────────────────────────────────────────

def generate_summary(
    name: str, years: float, skills: list,
    missing: list, score: float, rec_label: str
) -> str:
    """Generate a short natural-language candidate summary."""
    top_skills = ", ".join(skills[:4]) if skills else "various areas"
    gap_str = (
        f" Key gaps include {', '.join(missing[:3])}."
        if missing else " No critical skill gaps identified."
    )
    return (
        f"{name} brings {years:.0f}+ years of experience with expertise in "
        f"{top_skills}. ATS match: {score:.0f}% — {rec_label}.{gap_str}"
    )
