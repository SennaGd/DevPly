import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database.db"

def connect_db() -> sqlite3.Connection:
	return sqlite3.connect(DB_PATH)

def get_user(username: str) -> tuple | None:
	conn = connect_db()
	cur = conn.cursor()

	user = cur.execute(
				"SELECT * FROM users WHERE username = ?",
				(username,)
			).fetchone()
	conn.close()

	return user

def create_user():
	...
	
	
