import os
import sqlite3

API_KEY = os.environ["OPENAI_API_KEY"]


def get_user(name):
    # Input validation
    if not isinstance(name, str):
        raise ValueError("name must be a string")
    if not name.strip():
        raise ValueError("name must not be empty")
    if len(name) > 256:
        raise ValueError("name must not exceed 256 characters")

    # Safe parameterized query with proper connection handling
    try:
        with sqlite3.connect("db.sqlite") as conn:
            return conn.execute(
                "SELECT * FROM users WHERE name = ?",
                (name,),
            ).fetchall()
    except sqlite3.Error as e:
        raise RuntimeError("Database query failed") from e