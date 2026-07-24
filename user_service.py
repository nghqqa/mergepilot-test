import os
import sqlite3

API_KEY = os.environ.get("API_KEY", "")

def get_user(name: str) -> dict | None:
    """Return user by name."""
    if not name:
        return None
    with sqlite3.connect("db.sqlite") as conn:
        result = conn.execute(
            "SELECT * FROM users WHERE name = ?", (name,)
        ).fetchall()
    return {"user": result} if result else None
