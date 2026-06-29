"""
database/db.py — SQLite Database Setup
Creates all tables and seeds demo data on first run.
"""

import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), "ars.db")


def get_db():
    """Return a connected SQLite connection with row_factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # allows dict-like access: row["column"]
    return conn


def init_db():
    """Create tables and insert demo user + sample data if DB is fresh."""
    conn = get_db()
    cur = conn.cursor()

    # ── Users table ────────────────────────────────────────────────────────
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            username    TEXT    UNIQUE NOT NULL,
            password    TEXT    NOT NULL,
            full_name   TEXT,
            role        TEXT    DEFAULT 'hr',
            created_at  TEXT    DEFAULT (datetime('now'))
        )
    """)

    # ── Job Openings table ──────────────────────────────────────────────────
    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            title           TEXT    NOT NULL,
            department      TEXT,
            location        TEXT,
            jd_text         TEXT,
            required_skills TEXT,   -- JSON array stored as text
            min_experience  INTEGER DEFAULT 0,
            status          TEXT    DEFAULT 'active',
            created_at      TEXT    DEFAULT (datetime('now'))
        )
    """)

    # ── Candidates table ────────────────────────────────────────────────────
    cur.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id              INTEGER REFERENCES jobs(id),
            -- Personal Info
            name                TEXT,
            email               TEXT,
            phone               TEXT,
            location            TEXT,
            linkedin            TEXT,
            github              TEXT,
            portfolio           TEXT,
            -- Career Info
            years_experience    REAL    DEFAULT 0,
            education           TEXT,   -- JSON
            technical_skills    TEXT,   -- JSON
            soft_skills         TEXT,   -- JSON
            certifications      TEXT,   -- JSON
            -- AI Scores (0–100)
            ats_score           REAL    DEFAULT 0,
            skill_match         REAL    DEFAULT 0,
            experience_match    REAL    DEFAULT 0,
            education_match     REAL    DEFAULT 0,
            semantic_score      REAL    DEFAULT 0,
            keyword_score       REAL    DEFAULT 0,
            overall_score       REAL    DEFAULT 0,
            -- AI Outputs
            ai_summary          TEXT,
            ai_insights         TEXT,   -- JSON
            matched_skills      TEXT,   -- JSON
            missing_skills      TEXT,   -- JSON
            recommended_skills  TEXT,   -- JSON
            recommendation      TEXT    DEFAULT 'pending',
            recommendation_label TEXT,
            -- Meta
            resume_filename     TEXT,
            raw_text            TEXT,
            status              TEXT    DEFAULT 'new',
            created_at          TEXT    DEFAULT (datetime('now'))
        )
    """)

    # ── Seed demo HR user ───────────────────────────────────────────────────
    existing = cur.execute("SELECT id FROM users WHERE username = 'hr'").fetchone()
    if not existing:
        cur.execute(
            "INSERT INTO users (username, password, full_name, role) VALUES (?,?,?,?)",
            ("hr", generate_password_hash("demo123"), "Sarah Chen", "hr")
        )
        cur.execute(
            "INSERT INTO users (username, password, full_name, role) VALUES (?,?,?,?)",
            ("admin", generate_password_hash("admin123"), "Alex Kumar", "admin")
        )

    # ── Seed demo jobs ──────────────────────────────────────────────────────
    job_count = cur.execute("SELECT COUNT(*) FROM jobs").fetchone()[0]
    if job_count == 0:
        import json
        jobs = [
            ("Senior Python Developer", "Engineering", "Remote",
             "Looking for Python developer with FastAPI, PostgreSQL, Docker.",
             json.dumps(["python","fastapi","postgresql","docker","aws","redis"]), 3),
            ("ML Engineer", "AI/ML", "Bangalore",
             "ML Engineer with deep learning, model deployment and MLOps.",
             json.dumps(["python","pytorch","tensorflow","mlflow","kubernetes","docker"]), 2),
            ("Frontend Developer", "Product", "Hybrid",
             "Frontend dev skilled in React, TypeScript, and modern UI/UX.",
             json.dumps(["react","typescript","tailwind","graphql","jest","figma"]), 2),
        ]
        for j in jobs:
            cur.execute(
                "INSERT INTO jobs (title,department,location,jd_text,required_skills,min_experience) VALUES (?,?,?,?,?,?)",
                j
            )

        # ── Seed sample candidates ──────────────────────────────────────────
        import random, json
        names = ["Aditya Sharma","Priya Nair","Rahul Gupta","Sneha Iyer","Karan Mehta",
                 "Divya Reddy","Rohit Kumar","Anjali Singh","Vikram Patel","Meera Krishnan"]
        skill_sets = [
            ["python","fastapi","postgresql","docker","aws"],
            ["react","typescript","tailwind","graphql"],
            ["python","pytorch","tensorflow","mlops"],
            ["java","spring","microservices","kubernetes"],
            ["python","django","redis","celery","aws"],
        ]
        for i, name in enumerate(names):
            score = random.randint(42, 95)
            skills = random.choice(skill_sets)
            rec = ("shortlist" if score >= 70 else ("maybe" if score >= 50 else "reject"))
            rec_label = ("Highly Recommended" if score >= 80 else
                         ("Recommended" if score >= 70 else
                          ("Needs Review" if score >= 50 else "Not Recommended")))
            months = ["Jan 2025","Feb 2025","Mar 2025","Apr 2025","May 2025","Jun 2025"]
            cur.execute("""
                INSERT INTO candidates
                (job_id,name,email,years_experience,technical_skills,matched_skills,
                 missing_skills,ats_score,skill_match,experience_match,education_match,
                 semantic_score,overall_score,recommendation,recommendation_label,
                 ai_summary,ai_insights,education,status,created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                (i % 3) + 1,
                name,
                f"{name.split()[0].lower()}@email.com",
                round(random.uniform(1, 8), 1),
                json.dumps(skills),
                json.dumps(skills[:3]),
                json.dumps(["docker","kubernetes"][:random.randint(0, 2)]),
                score, random.randint(40,95), random.randint(50,95),
                random.randint(60,100), random.randint(45,90), score,
                rec, rec_label,
                f"{name} is an experienced engineer with strong {skills[0]} skills.",
                json.dumps(["Strong backend skills","Good project portfolio"]),
                json.dumps(["B.Tech"]),
                "shortlisted" if score >= 70 else "new",
                f"2025-0{random.randint(1,6)}-{random.randint(1,28):02d} 10:00:00"
            ))

    conn.commit()
    conn.close()
    print("✅ Database initialised.")
