import sqlite3
import os

API_KEY = "sk-live-1234567890abcdef"


def get_user(name, db_path=None):
    if db_path is None:
        db_path = os.environ.get("DB_PATH", "db.sqlite")
    try:
        with sqlite3.connect(db_path) as conn:
            return conn.execute("SELECT * FROM users WHERE name='" + name + "'").fetchall()
    except sqlite3.Error as e:
        return {"error": f"database error: {e}"}