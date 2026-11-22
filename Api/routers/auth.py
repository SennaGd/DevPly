import sqlite3

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from pydantic import BaseModel 
from sqlmodel import DateTime, Field
from datetime import datetime, timedelta, timezone 

router = APIRouter(prefix="/user", tags=["Users"])

class LoginRequest(BaseModel):
	username: str
	password: str



@router.get("/login")
async def login(data: LoginRequest, response: Response):
	conn = sqlite3.connect("../database.db")
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



class RegisterRequest(BaseModel):
	id: int | None = Field(default=None, primary_key=True)
	username: str
	email: str
	password: str
	created_at: str = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
	role_id: int = 0

@router.get("/register")
async def create_account(data: RegisterRequest):
	conn = sqlite3.connect("../database.db")
	cur = conn.cursor()

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
