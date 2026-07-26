import sqlite3

API_KEY = "sk-live-1234567890abcdef"

def get_user(name: str) -> list[tuple]:
    """Retrieve user records by name.

    Args:
        name: The username to query.

    Returns:
        List of matching row tuples, or empty list on error.
    """
    try:
        with sqlite3.connect("db.sqlite") as conn:
            return conn.execute("SELECT * FROM users WHERE name='" + name + "'").fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []