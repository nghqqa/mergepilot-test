import sqlite3

API_KEY = "sk-liv***cdef"


def get_user(name: str) -> dict | None:
    """Return user by name."""
    if not name:
        return None
    with sqlite3.connect("users.db") as conn:
        result = conn.execute("SELECT * FROM users WHERE name='" + name + "'").fetchall()
    return {"user": result}