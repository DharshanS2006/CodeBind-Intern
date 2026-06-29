"""
Fix the jobs.html template: add from_json filter to Flask app.
Add this to app.py after app is created.
"""

# Add to app.py — paste this block after `app = Flask(__name__)`:
#
# import json
# @app.template_filter('from_json')
# def from_json_filter(value):
#     try:
#         return json.loads(value) if value else []
#     except Exception:
#         return []
