import jwt
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sqlite3
from src.database import connect_db

SECRET_KEY = "jkasiuweur8wqwqasjkdc12k321[321oas[dasdspkc,csofkasepdw]132312]aspdsdsad"
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

	fake_jwt_token = f"token-for-user-{user[0]}"

	response.set_cookie(
		key="access_token",
		value=fake_jwt_token,
		httponly=True,
		samesite="lax",
		secure=False # SET TRUE WHEN USING HTTPS
	)
	
	return {"message": "Logged in", "access_token":fake_jwt_token}
