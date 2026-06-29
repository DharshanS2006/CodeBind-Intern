"""
routes/auth.py — Login / Logout routes
"""

from flask import (Blueprint, render_template, request,
                   redirect, url_for, session, flash)
from database.db import get_db
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("dashboard.index"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"]   = user["id"]
            session["username"]  = user["username"]
            session["full_name"] = user["full_name"]
            session["role"]      = user["role"]
            flash(f"Welcome back, {user['full_name']}!", "success")
            return redirect(url_for("dashboard.index"))
        else:
            flash("Invalid username or password.", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
