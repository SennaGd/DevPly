from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3
from src.database import connect_db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.get("/init")
async def init_db():

	conn = connect_db() 
	cur = conn.cursor()
#	cur.execute("CREATE TABLE users(username, email, password)")
	cur.execute("INSERT INTO users VALUES ('dev', 'dev@ply.com', '12345')")
	conn.commit()

	user = cur.execute("SELECT * FROM users WHERE username = 'dev'").fetchone()
	conn.close()

	return {"user":user}

@app.get("/user/{username}")
async def fetch_user(username):
	conn = connect_db()
	cur = conn.cursor()

	user = cur.execute(f"SELECT * FROM users WHERE username = '{username}'").fetchone()
	conn.close()

	return {"user":user}
	
@app.post("/user/{username}")
async def fetch_user2(username):
	conn = connect_db()
	cur = conn.cursor()

	user = cur.execute(f"SELECT * FROM users WHERE username = '{username}'").fetchone()
	conn.close()

	return {"user":user}

