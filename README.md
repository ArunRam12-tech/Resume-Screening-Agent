# 🤖 HireSense AI – Intelligent Resume Screening Agent

### AI-Powered Resume Ranking using NLP, Sentence Transformers & Semantic Similarity

![Python](https://img.shields.io/badge/Python-3.11-blue)
![NLP](https://img.shields.io/badge/NLP-SentenceTransformers-green)
![spaCy](https://img.shields.io/badge/spaCy-3.x-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📖 Overview

HireSense AI is an intelligent Resume Screening Agent developed as part of the **Rooman Technologies AI Challenge**.

The system automatically analyzes multiple resumes, extracts candidate information, compares resumes against a Job Description using **Natural Language Processing (NLP)**, and ranks candidates based on weighted evaluation metrics.

Instead of traditional keyword matching, HireSense AI uses **Sentence Transformers** to understand the semantic meaning of resumes and job descriptions, resulting in more accurate candidate ranking.

---

# 🎯 Problem Statement

Recruiters spend significant time manually screening resumes.

HireSense AI automates this process by:

- Parsing resumes
- Extracting candidate information
- Comparing resumes with a Job Description
- Ranking candidates
- Providing AI-powered recommendations

---

# ✨ Features

- 📄 Parse PDF, DOCX and TXT resumes
- 👤 Extract Candidate Name
- 📧 Extract Email Address
- 📱 Extract Phone Number
- 💻 Extract Technical Skills
- 💼 Detect Experience
- 🎓 Detect Educational Qualification
- 🤖 Semantic Similarity using Sentence Transformers
- 📊 Weighted Candidate Scoring
- 📈 Candidate Ranking
- 🧠 AI Recruiter Recommendation
- ❌ Missing Skill Detection
- 📁 CSV Export
- 📂 Batch Resume Processing (10+ resumes supported)

---

# 🏗 System Architecture

```
                 Job Description
                        │
                        ▼
               Feature Extraction
                        │
                        ▼
 Resume Parser (PDF/DOCX/TXT)
                        │
                        ▼
         Candidate Information Extraction
      ├── Name
      ├── Email
      ├── Phone
      ├── Skills
      ├── Experience
      └── Education
                        │
                        ▼
      Sentence Transformer (all-MiniLM-L6-v2)
                        │
                        ▼
          Cosine Similarity Calculation
                        │
                        ▼
          Weighted Candidate Scoring
                        │
                        ▼
              Candidate Ranking
                        │
                        ▼
         AI Recruiter Recommendation
                        │
                        ▼
             Ranked CSV Output
```

---

# 📂 Project Structure

```
ResumeScreeningAgent/

│
├── ai/
│   └── explanation.py
│
├── assets/
│   └── style.css
│
├── data/
│   ├── jobs/
│   ├── resumes/
│   ├── output/
│   └── skills/
│       └── skills.csv
│
├── models/
│   ├── similarity.py
│   ├── scoring.py
│   └── ranking.py
│
├── parser/
│   ├── pdf_parser.py
│   ├── docx_parser.py
│   └── resume_parser.py
│
├── preprocessing/
│   └── feature_extractor.py
│
├── utils/
│   ├── config.py
│   └── export.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── TRADEOFF.md
```

---

# 🧠 AI & NLP Model

### Sentence Transformer

```
all-MiniLM-L6-v2
```

### Similarity Metric

```
Cosine Similarity
```

### Why Sentence Transformers?

Traditional ATS systems rely only on keyword matching.

Sentence Transformers understand semantic meaning, enabling more accurate candidate-job matching.

---

# 📊 Candidate Scoring Method

| Component | Weight |
|-----------|--------|
| Semantic Similarity | 40% |
| Skill Match | 30% |
| Experience | 15% |
| Education | 10% |
| Projects | 5% |

Final Score

```
Overall Score =
Semantic +
Skills +
Experience +
Education +
Projects
```

---

# 🔄 Workflow

1. Load Job Description
2. Parse Resume
3. Extract Candidate Information
4. Extract Skills
5. Compute Semantic Similarity
6. Calculate Weighted Score
7. Rank Candidates
8. Generate AI Recommendation
9. Export Results to CSV

---

# 📥 Sample Input

### Job Description

Software Engineer

Required Skills

- Java
- Python
- SQL
- REST API
- React
- Git
- Machine Learning

### Candidate Resumes

- Rahul Sharma.pdf
- Arun H.pdf
- Priya Nair.pdf
- Sneha Reddy.pdf
- Kiran Kumar.pdf

---

# 📤 Sample Output

```
Candidate Rankings

Rank Candidate               Score

1 Rahul Sharma               82.09%

2 Arun H                     76.55%

3 Priya Nair                 58.38%

4 Kiran Kumar                47.73%

5 Sneha Reddy                34.53%
```

---

# 🤖 AI Recommendation

```
Candidate

Rahul Sharma

Strengths

✔ Strong Skill Match

✔ Relevant Experience

✔ Excellent Education

✔ Good Semantic Match

Missing Skills

None

Recommendation

⭐⭐⭐⭐⭐

Proceed to Technical Interview
```

---

# 📁 Output

The application generates

```
ranked_candidates.csv
```

inside

```
data/output/
```

---

# ⚙ Technologies Used

- Python 3.11
- Sentence Transformers
- spaCy
- Scikit-learn
- Pandas
- NumPy
- pdfplumber
- python-docx
- PyPDF2
- Streamlit
- Plotly

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/ArunRam12-tech/Resume-Screening-Agent.git
```

Go to Project

```bash
cd Resume-Screening-Agent
```

Create Environment

```bash
conda create -n hiresense python=3.11
```

Activate Environment

```bash
conda activate hiresense
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# ▶️ Run the Project

### Command Line

```bash
python main.py
```

### Streamlit UI

```bash
streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots here after running the application.

```
screenshots/

├── dashboard.png

├── ranking.png

├── recommendation.png
```

---

# 🎯 Future Enhancements

- OCR support for scanned resumes
- Resume summarization using LLMs
- Recruiter Login System
- Interview Question Generator
- Email Notifications
- Cloud Database
- REST API
- Streamlit Dashboard Improvements
- Analytics Dashboard
- Multi-language Resume Support

---

# ⚖ Trade-offs

## Why Sentence Transformers?

Sentence Transformers provide semantic understanding instead of simple keyword matching, improving ranking accuracy.

## Why Cosine Similarity?

Cosine Similarity efficiently measures similarity between embedding vectors regardless of document length.

## Current Limitations

- Rule-based experience extraction
- Skills depend on predefined skills database
- No OCR for scanned resumes
- No external ATS integration
- No recruiter authentication

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

- Hugging Face
- Sentence Transformers
- spaCy
- Scikit-learn
- Streamlit
- Plotly
- Python Community

---

# 👨‍💻 Author

## Arun H

Computer Science Engineering Graduate

Skills

- Java
- Python
- SQL
- React.js
- Machine Learning
- Deep Learning
- NLP
- AI
- Git
- Power BI

GitHub

https://github.com/ArunRam12-tech

---

⭐ If you found this project useful, consider giving it a star.