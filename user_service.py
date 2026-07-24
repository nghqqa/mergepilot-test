import sqlite3
import os

# 修复:API_KEY 从环境变量读取,不再硬编码(原 sk-live 硬编码密钥)
API_KEY = os.environ.get("API_KEY", "")


def get_user(name):
    conn = sqlite3.connect("db.sqlite")
    # 修复:参数化查询,消除 SQL 注入(原字符串拼接)
    return conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall()