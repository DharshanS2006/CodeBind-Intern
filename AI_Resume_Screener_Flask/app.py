"""
app.py — Main Flask Application Entry Point
AI Resume Screening System — Final Year BSc CS (AI) Project
Author: Dharshan S | VIT Chennai | 24BCS1019
"""

from flask import Flask, redirect, url_for
from database.db import init_db
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.candidates import candidates_bp
from routes.jobs import jobs_bp
from routes.api import api_bp
import os, json

# ── App Initialization ─────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "ars-secret-key-2025-change-in-prod")
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB max upload

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# ── Custom Jinja2 Filters ──────────────────────────────────────────────────
@app.template_filter("from_json")
def from_json_filter(value):
    """Parse a JSON string in templates: {{ skills_json | from_json }}"""
    try:
        return json.loads(value) if value else []
    except Exception:
        return []

# ── Register Blueprints ────────────────────────────────────────────────────
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(candidates_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(api_bp)


@app.route("/")
def index():
    return redirect(url_for("auth.login"))


# ── Database Init ──────────────────────────────────────────────────────────
with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
