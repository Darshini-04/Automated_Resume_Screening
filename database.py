import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "database"
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "candidates.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            filename TEXT NOT NULL,
            match_score REAL NOT NULL,
            rank INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def save_candidates(results):
    connection = get_connection()
    cursor = connection.cursor()

    for candidate in results:
        cursor.execute("""
            INSERT INTO candidates (name, filename, match_score, rank)
            VALUES (?, ?, ?, ?)
        """, (
            candidate["name"],
            candidate["filename"],
            candidate["score"],
            candidate["rank"]
        ))

    connection.commit()
    connection.close()
