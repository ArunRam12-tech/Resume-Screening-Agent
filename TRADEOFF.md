# Trade-off Analysis

## Model Selection

### Sentence Transformers (all-MiniLM-L6-v2)

Chosen because it captures semantic meaning between resumes and job descriptions rather than relying only on keyword matching.

### Alternative Models Considered

### TF-IDF

Pros
- Fast
- Lightweight

Cons
- Cannot understand context
- Keyword matching only

### BERT

Pros
- High accuracy

Cons
- Slow inference
- Large model size

### OpenAI Embeddings

Pros
- Excellent semantic understanding

Cons
- Requires API key
- Paid service
- Internet dependency

---

# Similarity Metric

Cosine Similarity is used because it effectively compares embedding vectors irrespective of document length.

---

# Resume Parsing

Current Approach

- pdfplumber for PDF
- python-docx for DOCX

Pros

- Fast
- Reliable
- Easy to maintain

Limitations

- Scanned PDFs require OCR
- Complex layouts may reduce extraction quality

---

# Skills Extraction

Current

CSV-based Skills Database

Advantages

- Easy to maintain
- Recruiters can add skills without changing code
- Scalable

Future Improvement

Use Named Entity Recognition (NER) to dynamically detect technologies.

---

# Experience Detection

Current

Rule-based extraction

Advantages

- Simple
- Fast

Limitations

- Doesn't calculate exact employment duration
- Doesn't understand date ranges

Future Improvement

Parse employment timelines and compute total years automatically.

---

# Education Detection

Current

Keyword matching

Future Improvement

Normalize degrees such as

- BE
- BTech
- Bachelor of Engineering

into one standard representation.

---

# Candidate Ranking

Weighted Scoring

| Component | Weight |
|-----------|--------|
| Semantic Similarity | 40% |
| Skill Match | 30% |
| Experience | 15% |
| Education | 10% |
| Projects | 5% |

This weighted approach provides better explainability compared to relying solely on semantic similarity.

---

# Future Scope

- Streamlit Dashboard
- Recruiter Login
- Interview Scheduling
- Email Notifications
- Resume Summarization using LLMs
- OCR for scanned resumes
- Cloud Deployment
- Docker Support
- REST API