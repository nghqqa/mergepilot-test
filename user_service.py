import sqlite3

API_KEY = "sk-live-1234567890abcdef"

def get_user(name):
    conn = sqlite3.connect("db.sqlite")
    return conn.execute("SELECT * FROM users WHERE name='" + name + "'").fetchall()