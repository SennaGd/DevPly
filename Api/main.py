import jwt
from datetime import datetime, timedelta, timezone 

from fastapi import FastAPI, HTTPException, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field
from pydantic import BaseModel

import sqlite3
from src.database import connect_db
import logging

logger = logging.getLogger(__name__)

SECRET_KEY = "change-this-to-a-long-random-secret-string"
ALGORITHM = "HS256"

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
    allow_origins=[
		"http://localhost:5173",
		"http://127.0.0.1:5173"
	],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
	username: str
	password: str

class RegisterRequest(BaseModel):
	id: int | None = Field(default=None, primary_key=True)
	username: str
	email: str
	password: str
	created_at: str = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
	role_id: int = 0


@app.post("/login")
async def login(data: LoginRequest, response: Response):
	conn = connect_db()
	cur = conn.cursor()

	user = cur.execute(
				"SELECT * FROM users WHERE username = ?",
				(data.username,)
			).fetchone()
	conn.close()

	if not user or user[3] != data.password:
		raise HTTPException(401, "Invalid credentials balls")

	payload = {
		"uid": str(user[0]), # User ID
		"username":user[1],
		"role_id":user[5],
		"exp":datetime.now(timezone.utc) + timedelta(hours=24)
	} 
	jwt_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)

	response.set_cookie(
		key="access_token",
		value=jwt_token,
		httponly=True,
		samesite="lax",
		secure=False # SET TRUE WHEN USING HTTPS
	)
	
	return {"message": "Logged in"} 

@app.post("/register")
async def create_account(data: RegisterRequest):
	conn = connect_db()
	cur = conn.cursor()
	logger.info(f"data {data}")
	user = cur.execute(
			"SELECT * FROM users WHERE username = ?",
			(data.username,)
		).fetchone()

	if user == None:
		cur.execute(
			"INSERT INTO users VALUES (?,?,?,?,?,?)",
			(data.id, data.username, data.email, data.password, data.created_at, data.role_id,)
		)
		conn.commit()
		conn.close()

		return {"message": "User Created"}
	else:
		raise HTTPException(status_code=401, detail="Account already exists")


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

@app.get("/user/role")
async def get_user_role(access_token: str | None = Cookie(default=None)):
	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	conn = connect_db()
	cur = conn.cursor()

	try:
		payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)

	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")


class ProjectRequest(BaseModel):
	id: int | None = Field(default=None, primary_key=True)
	title: str
	description: str
	creator_id: int | None = None
	created_at: str = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

@app.post("/create_project")
async def create_project(projectData: ProjectRequest, access_token: str | None = Cookie(default=None)):
	conn = connect_db()
	cur = conn.cursor()

	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try: 
		payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
		projectData.creator_id = payload["uid"]

	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")
	
	if projectData.creator_id == None: 
		raise HTTPException(401, "Missing UID")

	project = cur.execute(
			"SELECT * FROM projects WHERE title = ?",
			(projectData.title,)
		).fetchone()

	if project != None:
		return {"message":"project already exists"}

	cur.execute(
		"INSERT INTO projects VALUES (?,?,?,?,?)", (
			projectData.id, 
			projectData.title, 
			projectData.description, 
			projectData.creator_id, 
			projectData.created_at
		)
	)
	conn.commit()
	conn.close()

	return {"message":"Created new project successfully!"}

@app.get("/fetch_projects")
async def fetch_user_projects(access_token: str | None = Cookie(default=None)):
	conn = connect_db()
	cur = conn.cursor()

	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try: 
		payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
		userId = payload["uid"]	

		projects = cur.execute(
				"SELECT * FROM projects WHERE creator_id = ?", (userId,)
		).fetchall()

		return {"message":projects}
	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")

