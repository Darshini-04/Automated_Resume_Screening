import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    """Basic NLP preprocessing for matching."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def rank_resumes(job_description, resumes):
    """Calculate TF-IDF cosine similarity and rank resumes."""
    documents = [job_description] + [resume["text"] for resume in resumes]
    documents = [preprocess_text(doc) for doc in documents]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    job_vector = matrix[0]
    resume_vectors = matrix[1:]

    scores = cosine_similarity(job_vector, resume_vectors).flatten()

    results = []
    for resume, score in zip(resumes, scores):
        results.append({
            "name": resume["name"],
            "filename": resume["filename"],
            "score": round(float(score) * 100, 2)
        })

    results.sort(key=lambda item: item["score"], reverse=True)

    for rank, result in enumerate(results, start=1):
        result["rank"] = rank

    return results
