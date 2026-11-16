import jwt
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, HTTPException, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sqlite3
from src.database import connect_db

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


@app.post("/login")
async def login(data: LoginRequest, response: Response):
	conn = connect_db()
	cur = conn.cursor()

	user = cur.execute(
				"SELECT * FROM users WHERE username = ?",
				(data.username,)
			).fetchone()
	conn.close()

	if not user or user[2] != data.password:
		raise HTTPException(401, "Invalid credentials")

	payload = {
		"sub": str(user[0]),
		"username":user[1],
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

@app.get("/user")
async def get_current_user(access_token: str | None = Cookie(default=None)):
	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try: 
		payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
		return {"id":payload["sub"], "username":payload["username"]}

	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")
