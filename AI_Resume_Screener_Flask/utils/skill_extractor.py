"""
utils/skill_extractor.py
Matches resume text against a curated skills database.
Extracts both technical and soft skills.
"""

# ── Technical Skills Database ────────────────────────────────────────────────
TECHNICAL_SKILLS = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "go", "rust",
    "kotlin", "swift", "r", "scala", "php", "ruby", "matlab", "perl",
    # Web Frameworks & Libraries
    "react", "angular", "vue", "nextjs", "svelte", "node.js", "express",
    "fastapi", "django", "flask", "spring", "laravel", "rails",
    # Databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
    "cassandra", "dynamodb", "sqlite", "oracle", "nosql",
    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ansible",
    "jenkins", "ci/cd", "github actions", "linux", "bash",
    # AI / ML / Data Science
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "pytorch", "keras", "scikit-learn", "xgboost",
    "pandas", "numpy", "matplotlib", "seaborn", "plotly",
    "mlops", "mlflow", "airflow", "spark", "hadoop", "kafka",
    "huggingface", "langchain", "openai", "llm",
    # Tools & Platforms
    "git", "github", "gitlab", "jira", "figma", "photoshop",
    "rest api", "graphql", "microservices", "agile", "scrum",
    "tableau", "power bi", "excel", "bigquery", "snowflake",
    "celery", "rabbitmq", "nginx", "prometheus", "grafana",
    # Frontend Specifics
    "html", "css", "tailwind", "bootstrap", "sass",
]

# ── Soft Skills Database ─────────────────────────────────────────────────────
SOFT_SKILLS = [
    "communication", "leadership", "teamwork", "problem solving",
    "critical thinking", "time management", "adaptability", "creativity",
    "collaboration", "attention to detail", "project management",
    "presentation", "mentoring", "conflict resolution", "analytical",
]


def extract_technical_skills(text: str) -> list:
    """Return list of technical skills found in the text (case-insensitive)."""
    text_lower = text.lower()
    return sorted([skill for skill in TECHNICAL_SKILLS if skill in text_lower])


def extract_soft_skills(text: str) -> list:
    """Return list of soft skills found in the text."""
    text_lower = text.lower()
    return [skill for skill in SOFT_SKILLS if skill in text_lower]


def get_matched_skills(resume_skills: list, required_skills: list) -> list:
    """Return skills present in both resume and JD."""
    resume_set = {s.lower() for s in resume_skills}
    return [s for s in required_skills if s.lower() in resume_set]


def get_missing_skills(resume_skills: list, required_skills: list) -> list:
    """Return skills required by the JD but missing from the resume."""
    resume_set = {s.lower() for s in resume_skills}
    return [s for s in required_skills if s.lower() not in resume_set]


def get_recommended_skills(missing_skills: list) -> list:
    """Return learning recommendations based on missing skills."""
    recommendations = {
        "docker": "Learn Docker via docs.docker.com",
        "kubernetes": "Try Kubernetes tutorials at kubernetes.io",
        "aws": "Start with AWS Free Tier at aws.amazon.com",
        "pytorch": "Learn PyTorch at pytorch.org/tutorials",
        "tensorflow": "Explore TensorFlow at tensorflow.org/learn",
        "react": "Start React at react.dev",
        "typescript": "Learn TypeScript at typescriptlang.org",
        "fastapi": "FastAPI docs at fastapi.tiangolo.com",
        "mlflow": "Try MLflow at mlflow.org",
    }
    return [recommendations[s] for s in missing_skills if s in recommendations]
