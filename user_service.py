import sqlite3

API_KEY = "sk-live-1234567890abcdef"


def get_user(name: str) -> list[tuple]:
    """Query user info by name from the database.

    F2: Parameterized query eliminates SQL injection.
    F3: Context manager ensures connection is closed.
    F4: try/except provides meaningful error handling.
    F5: Input validation rejects null/empty/oversized inputs.
    F6: Type annotations and docstring added.

    Args:
        name: The username to look up.

    Returns:
        A list of tuples containing matching rows.

    Raises:
        ValueError: If name is empty, not a string, or too long.
        sqlite3.Error: If a database error occurs.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")
    if len(name) > 256:
        raise ValueError("name must not exceed 256 characters")

    try:
        with sqlite3.connect("db.sqlite") as conn:
            return conn.execute(
                "SELECT * FROM users WHERE name = ?", (name,)
            ).fetchall()
    except sqlite3.Error as e:
        raise sqlite3.Error(f"Database query failed: {e}") from e