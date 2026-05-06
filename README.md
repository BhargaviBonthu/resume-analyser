# AI Resume Analyzer

An AI-powered resume analysis application built using Streamlit, Ollama, and local LLMs.

This application allows users to upload resumes in PDF format and receive AI-generated feedback including:
- Technical strengths
- Missing industry-relevant skills
- Resume improvement suggestions
- ATS optimization tips
- Recommended certifications
- Suggested job roles

The project uses a locally running language model through Ollama, enabling offline AI inference without relying on paid cloud APIs.

---

# Features

- PDF resume upload
- Multi-resume comparison
- Resume text extraction
- AI-powered analysis
- Local LLM inference using Ollama
- Streamlit-based interactive UI
- Real-time feedback generation
- Offline processing support

---

# Tech Stack

- Python
- Streamlit
- Ollama
- Phi3 LLM
- PyPDF2

---

# Project Workflow

1. User uploads resume PDF
2. Application extracts resume text
3. Prompt is generated dynamically
4. Local LLM processes resume content
5. AI-generated analysis is displayed in UI

---

# Installation

## Clone Repository

```cmd
cd resume-analyzer
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```cmd
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama.

Run local model:

```bash
ollama run phi3
```

---

## Run Application

```cmd
streamlit run app.py
```

---

# Future Improvements


- Resume scoring system
- Skill extraction dashboard
- Downloadable AI feedback reports
- Cloud deployment
- RAG-based resume querying

---

# Learning Outcomes

This project helped in understanding:
- Local LLM integration
- Prompt engineering
- PDF processing
- Streamlit application development
- AI inference workflows
- Backend/frontend interaction

---

# Author

Bhargavi Bonthu
