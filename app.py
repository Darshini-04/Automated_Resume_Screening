from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pathlib import Path

from resume_parser import extract_text_from_pdf
from matcher import rank_resumes
from database import init_db, save_candidates

app = Flask(__name__)
app.secret_key = "resume-screening-demo"

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "resumes"
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {"pdf"}

init_db()

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_description = request.form.get("job_description", "").strip()
        uploaded_files = request.files.getlist("resumes")

        if not job_description:
            flash("Please enter a job description.")
            return redirect(url_for("index"))

        valid_files = [
            f for f in uploaded_files
            if f and f.filename and allowed_file(f.filename)
        ]

        if not valid_files:
            flash("Please upload at least one PDF resume.")
            return redirect(url_for("index"))

        resumes = []

        for file in valid_files:
            filename = secure_filename(file.filename)
            path = UPLOAD_DIR / filename
            file.save(path)

            text = extract_text_from_pdf(path)
            resumes.append({
                "name": Path(filename).stem,
                "filename": filename,
                "text": text
            })

        results = rank_resumes(job_description, resumes)
        save_candidates(results)

        return render_template("results.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
