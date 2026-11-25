import jwt, os, sqlite3
from datetime import datetime, timedelta, timezone 
from fastapi import FastAPI, HTTPException, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field
from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path
from utils.database import connect_db
from utils.env import ADDRESS,WEB_PORT

from routes.auth import auth_routes
from routes.projects import project_routes 

SECRET_KEY = "change-this-to-a-long-random-secret-string"
ALGORITHM = "HS256"

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
    allow_origins=[
		ADDRESS,
		f"http://127.0.0.1:{WEB_PORT}"
	],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(project_routes.router)

#@app.post("/register")
#async def create_account(data: RegisterRequest):
#	conn = connect_db()
#	cur = conn.cursor()
#
#	user = cur.execute(
#			"SELECT * FROM users WHERE username = ?",
#			(data.username,)
#		).fetchone()
#
#	if user == None:
#		cur.execute(
#			"INSERT INTO users VALUES (?,?,?,?,?,?)",
#			(data.id, data.username, data.email, data.password, data.created_at, data.role_id,)
#		)
#		conn.commit()
#		conn.close()
#
#		return {"message": "User Created"}
#	else:
#		raise HTTPException(status_code=401, detail="Account already exists")


@app.get("/user")
async def get_current_user(access_token: str | None = Cookie(default=None)):
	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try: 
		payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
		return {"id":payload["uid"], "username":payload["username"], "role_id":payload["role_id"]}

	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")

@app.get("/roles")
async def get_roles():
	conn = connect_db()
	cur = conn.cursor()

	roles = cur.execute(
		"SELECT * FROM roles;"
	)

	return { "message":roles }


