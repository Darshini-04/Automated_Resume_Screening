# Automated Resume Screening & Ranking System

A basic ATS-style web application that compares candidate resumes with a job description and ranks candidates using TF-IDF and cosine similarity.

## Features

- Upload multiple PDF resumes
- Enter a job description
- Extract resume text using PyPDF
- Perform basic NLP preprocessing
- Convert text to TF-IDF vectors
- Calculate cosine similarity
- Rank candidates by match score
- Store screening results in SQLite
- Simple Flask web interface

## Project Flow

Job Description + Resume PDFs  
↓  
PyPDF Text Extraction  
↓  
NLP Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Cosine Similarity  
↓  
Match Score  
↓  
SQLite Database  
↓  
Ranked Candidates

## Technologies

- Python
- Flask
- PyPDF
- Scikit-learn
- TF-IDF
- Cosine Similarity
- SQLite
- HTML/CSS

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Open the local Flask address shown in the terminal.

## Important note

This is a prototype demonstrating resume-to-job-description text similarity. The match score is a similarity score, not a hiring probability or an objective measure of candidate quality.
