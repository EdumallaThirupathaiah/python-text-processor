import sqlite3
from datetime import datetime

DB_NAME = "text_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS processed_text (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        raw_content TEXT,
        processed_tokens TEXT,
        sentiment_score INTEGER,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_data(raw, processed, score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO processed_text (raw_content, processed_tokens, sentiment_score, timestamp)
    VALUES (?, ?, ?, ?)
    """, (raw, processed, score, datetime.now()))

    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM processed_text")
    data = cursor.fetchall()

    conn.close()
    return data
