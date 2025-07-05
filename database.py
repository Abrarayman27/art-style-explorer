import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("/app/db/predictions.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sepal_length FLOAT,
            sepal_width FLOAT,
            petal_length FLOAT,
            petal_width FLOAT,
            prediction TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_prediction(sepal_length, sepal_width, petal_length, petal_width, prediction):
    conn = sqlite3.connect("/app/db/predictions.db")
    cursor = conn.cursor()
    timestamp = datetime.utcnow().isoformat()
    cursor.execute("""
        INSERT INTO predictions (sepal_length, sepal_width, petal_length, petal_width, prediction, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (sepal_length, sepal_width, petal_length, petal_width, prediction, timestamp))
    conn.commit()
    conn.close()

# Initialize database
init_db()
