# Quamrul Hoda — Personal AI & Machine Learning Portfolio

A modern, production-grade personal portfolio website showcasing expertise in AI Engineering, Machine Learning, Agentic AI, NLP, and RAG Systems. Built with Python (Flask) backend and clean HTML5, CSS3, JavaScript frontend.

---

## Features

- Modern Aesthetic: SaaS-style clean light mode layout with smooth micro-animations, glassmorphism elements, and subtle gradient highlights.
- Hero Section: Two-column responsive hero featuring profile image, key stats, tech focus, and direct CTAs.
- About Me & Current Focus: Highlights core background, active technical focus areas (LangGraph, Agentic AI, RAG), and contact chips.
- Education Section: Dedicated academic background showcase (B.Tech in Computer Science & Engineering).
- Core Skills Grid: Categorized proficiency cards covering AI/NLP, Agentic Frameworks, ML/DL, MLOps, Databases, and Async Languages.
- Work Experience Timeline: Structured career journey detailing internships, key contributions, and metrics.
- Featured Projects: Highlighting production-grade projects complete with previews, model metrics (e.g. 96% and 93% accuracy), and technology tags.
- Credentials & Certifications: Visual certification gallery displaying verified industry badges.
- Resume Integration: Built-in PDF viewing (/resume/view) and direct one-click downloading (/resume/download).
- Fully Responsive: Seamless layout adaptivity for desktops, tablets, and mobile devices.

---

## Tech Stack

- Backend: Python 3.x, Flask
- Frontend: HTML5, CSS3 (Vanilla CSS with CSS Variables), JavaScript (ES6+)
- Design Systems: Inter Font, SVG Icons, Responsive CSS Grid & Flexbox

---

## Project Structure

```text
personal_portfolio/
├── app.py                     # Flask application entry point & routes
├── requirements.txt           # Python dependencies (Flask)
├── resume/
│   └── quamrulHoda_resume.pdf  # PDF Resume source
├── static/
│   ├── style.css              # Main stylesheet (Design Tokens, Components, Media Queries)
│   ├── script.js              # Interactivity, Navbar toggle, Scroll animations
│   ├── profile.png            # Main hero profile image
│   ├── certificates/          # Certification images
│   ├── education/             # Education campus image
│   └── projects/              # Project preview images (chatbot, swiggy, wine quality, etc.)
└── templates/
    └── index.html             # Main portfolio single-page application template
```

---

## Getting Started

### Prerequisites

- Python 3.8+ installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/quamrl-hoda/personal_portfolio.git
   cd personal_portfolio
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open in browser:
   Navigate to `http://localhost:5000` in your web browser.

---

## Routes & Endpoints

| Route | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Main portfolio single-page application |
| `/resume/view` | `GET` | View PDF resume in browser |
| `/resume/download` | `GET` | Download PDF resume as an attachment |

---

## Contact & Socials

- Email: [quamrulhoda03@gmail.com](mailto:qhoda489@gmail.com)
- Phone: +91 9304192661
- GitHub: [github.com/quamrl-hoda](https://github.com/quamrl-hoda)
- LinkedIn: [linkedin.com/in/quamrul-hoda](https://linkedin.com/in/quamrul-hoda)

---

*Designed & Developed by Quamrul Hoda*
