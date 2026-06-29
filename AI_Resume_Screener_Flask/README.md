# 🎯 AI Resume Screening System

**Final Year BSc Computer Science (Artificial Intelligence) Project**  
Author: Dharshan S | VIT Chennai | Student ID: 24BCS1019

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?logo=flask)](https://flask.palletsprojects.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)](https://getbootstrap.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-NLP-orange)](https://scikit-learn.org)

---

## 📋 Project Abstract

An AI-powered web application that automates the resume screening process using Natural Language Processing and Machine Learning. HR teams can upload multiple resumes (PDF/DOCX), compare them against a Job Description, and instantly receive ATS scores, skill gap analysis, candidate rankings, and recruiter-friendly insights — all through a modern, professional dashboard.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Authentication** | HR Login with session management |
| 📊 **Dashboard** | Stats, charts (Chart.js), recent candidates |
| 📤 **Resume Upload** | Drag & drop PDF/DOCX, multi-file, AI analysis |
| 🤖 **AI Matching** | TF-IDF cosine similarity + weighted ATS score |
| 🏆 **Ranking** | Auto-rank all candidates by ATS score |
| 🔍 **Skill Gap Analysis** | Matched, missing, and recommended skills |
| 📝 **AI Summary** | Natural language candidate overview |
| 💡 **AI Insights** | Recruiter-friendly insight bullets |
| 🏷️ **Recommendations** | Highly Recommended / Recommended / Needs Review / Not Recommended |
| 🔎 **Search & Filter** | By name, score, recommendation, job |
| 📥 **CSV Export** | Download all candidates as spreadsheet |
| 🌙 **Dark/Light Mode** | Toggle with preference saved |
| 💼 **Job Openings** | Create and manage JD-linked job openings |

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5 · CSS3 · Bootstrap 5 · JavaScript · Chart.js |
| **Backend** | Python 3.10+ · Flask 3.0 |
| **Database** | SQLite (via Python `sqlite3`) |
| **AI / NLP** | scikit-learn (TF-IDF + Cosine Similarity) |
| **Parsing** | pdfplumber (PDF) · python-docx (DOCX) |
| **Auth** | Werkzeug password hashing + Flask sessions |

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/DharshanS2006/AI_Resume_Screener.git
cd AI_Resume_Screener
```

### 2. Create virtual environment
```bash
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

Open browser → **http://localhost:5000**

---

## 🔑 Demo Login Credentials

| Role | Username | Password |
|---|---|---|
| HR Manager | `hr` | `demo123` |
| Admin | `admin` | `admin123` |

---

## 📁 Project Structure

```
AI_Resume_Screener/
│
├── app.py                      # Flask app entry point
├── requirements.txt
├── README.md
│
├── database/
│   ├── __init__.py
│   └── db.py                   # SQLite schema + seed data
│
├── routes/
│   ├── __init__.py
│   ├── auth.py                 # Login / Logout
│   ├── dashboard.py            # Dashboard stats
│   ├── candidates.py           # Upload, list, detail, export
│   ├── jobs.py                 # Job openings CRUD
│   └── api.py                  # JSON API for charts
│
├── utils/
│   ├── __init__.py
│   ├── resume_parser.py        # PDF/DOCX text extraction + field parsing
│   ├── skill_extractor.py      # Skills database + matching
│   ├── resume_matcher.py       # TF-IDF scoring engine
│   ├── ai_pipeline.py          # Orchestrates full analysis
│   └── report_generator.py     # CSV + text report generation
│
├── templates/
│   ├── base.html               # Sidebar layout shell
│   ├── login.html              # Login page
│   ├── dashboard.html          # Dashboard with Chart.js
│   ├── upload.html             # Drag & drop upload
│   ├── upload_results.html     # Post-upload results
│   ├── candidates.html         # Filterable candidates table
│   ├── candidate_detail.html   # Full AI profile with score rings
│   ├── jobs.html               # Job openings grid
│   └── job_form.html           # Create/edit job form
│
├── static/
│   ├── css/style.css           # Custom design system
│   └── js/main.js              # Dark mode + Chart.js defaults
│
└── uploads/                    # Resume files (gitignored)
```

---

## 🔬 AI Scoring Algorithm

```
Resume (PDF/DOCX)
       │
       ▼  pdfplumber / python-docx
  Raw Text Extraction
       │
       ├── Name, Email, Phone, LinkedIn, GitHub  (regex)
       ├── Technical Skills  (keyword matching vs 80+ skill DB)
       ├── Soft Skills       (keyword matching)
       ├── Education         (degree keyword detection)
       ├── Experience Years  (regex + date range analysis)
       └── Certifications    (keyword matching)
       │
       ▼  scikit-learn TF-IDF Vectorizer (bigrams, 5000 features)
  Cosine Similarity vs Job Description text
       │
       ▼  Weighted Composite Scoring
  ┌────────────────────────────────────────┐
  │  Skill Match Score      ×  0.35        │
  │  Experience Match       ×  0.25        │
  │  Education Match        ×  0.15        │
  │  Semantic Similarity    ×  0.15        │
  │  Keyword Overlap        ×  0.10        │
  │  Certification Bonus    + max 8 pts    │
  └────────────────────────────────────────┘
       │
       ▼
  ATS Score (0–100) + Recommendation Label
```

---

## 🗄️ Database Schema (SQLite)

```sql
users       (id, username, password, full_name, role, created_at)
jobs        (id, title, department, location, jd_text,
             required_skills JSON, min_experience, status, created_at)
candidates  (id, job_id, name, email, phone, linkedin, github,
             years_experience, education JSON, technical_skills JSON,
             soft_skills JSON, certifications JSON,
             ats_score, skill_match, experience_match,
             education_match, semantic_score, keyword_score,
             matched_skills JSON, missing_skills JSON,
             recommendation, recommendation_label,
             ai_summary, ai_insights JSON,
             status, resume_filename, created_at)
```

---

## 📊 System Architecture

```
[Browser] ──HTTP──▶ [Flask App (app.py)]
                         │
            ┌────────────┼────────────────┐
            ▼            ▼                ▼
       [Routes]      [Utils/AI]       [Database]
       auth.py       pipeline.py      SQLite
       dashboard.py  parser.py        ars.db
       candidates.py matcher.py
       jobs.py       skill_extractor.py
            │
            ▼
       [Templates] ──Chart.js──▶ [Browser Charts]
       base.html
       dashboard.html …
```

---

## 🧪 Testing the Application

```bash
# 1. Start the server
python app.py

# 2. Login: http://localhost:5000/login
#    Username: hr   Password: demo123

# 3. Upload a sample resume
#    Go to Upload Resumes → drag a PDF/DOCX

# 4. Check Dashboard for charts and stats

# 5. View Candidates → click any row for full AI profile

# 6. Export → Download CSV from sidebar
```

---

## 🚀 Future Enhancements

- Integrate sentence-transformers (MiniLM) for deeper semantic matching
- Add spaCy NER for better name/org extraction
- Email notifications for shortlisted candidates
- API integration with LinkedIn / Naukri
- Multi-language resume support
- Interview scheduling module
- PostgreSQL for production deployment

---

## 📄 License

MIT — Free for academic and personal use.

---

*Built with Flask 🐍 · Bootstrap 5 🎨 · scikit-learn 🤖 · SQLite 🗄️*
