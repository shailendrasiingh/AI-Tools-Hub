# AI Tools Hub

🎓 AI Tools Hub — A student-focused platform to explore and access AI-powered tools for learning, productivity, and career growth. Built with **Flask, HTML, and CSS**.

---
# Project Overview

AI Tools Hub is a comprehensive Flask web application that serves as a curated directory for AI-powered tools and educational resources.
The platform organizes tools into three main categories to help students and professionals discover valuable resources for learning, career development, and academic support:

# 🛠️ Installation & Setup
## Prerequisites
Python 3.8 or higher
pip (Python package manager)

## Install dependencies
pip install -r requirements.txt

## Run the application
python app.py

## Access the application
Open your browser and navigate to: http://localhost:5000

# 🔧 Technical Details
## Backend (Flask)
#### Framework: Flask 3.0.3
#### Template Engine: Jinja2
#### Data Handling: JSON-based tool database
#### Routing: Dynamic category pages with search/filter functionality

## Frontend
#### Styling: Custom CSS with CSS variables
#### Typography: Poppins font family
#### Icons: Font Awesome 6.4.0
#### Responsive: Mobile-first design approach
## Key Dependencies
#### Flask==3.0.3
#### Werkzeug==3.0.3
#### Jinja2==3.1.4
#### itsdangerous==2.2.0
#### click==8.1.7

## 📁 Project Structure

```text
ai-tools-hub/
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
├── tools.json         # Tools database
├── README.md          # Project documentation
├── static/
│   └── style.css      # Main stylesheet
└── templates/
    ├── base.html      # Base template with navigation/footer
    ├── index.html     # Homepage
    ├── category.html  # Category pages template
    ├── about.html     # About page
    ├── contact.html   # Contact page
    ├── faq.html       # FAQ page
    ├── privacy.html   # Privacy policy
    └── terms.html     # Terms & conditions
