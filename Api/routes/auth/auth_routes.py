from sqlite3 import Connection, Cursor

from .auth_models import ( LoginRequest, RegisterRequest)
from fastapi import Cookie, Response, HTTPException, APIRouter, Depends

# helper functions
from utils.codec import decode_payload, encode_payload
from utils.database import get_user, connect_db
from utils.user import generate_access_token 

router = APIRouter(prefix="/users", tags=["Users", "Authentication"])

@router.post("/login")
async def login(data: LoginRequest, response: Response):
	user: tuple | None = get_user(data.username)

	if not user or user[3] != data.password:
		raise HTTPException(401, "Invalid credentials balls")

	payload: dict = generate_access_token(user) # dictionary with account info 
	jwt_token = encode_payload(payload)

	# cookie yummy 
	response.set_cookie(
		key="access_token",
		value=jwt_token,
		httponly=True,
		samesite="lax",
		secure=False # SET TRUE WHEN USING HTTPS
	)
	
	return {"message": "Logged in"} 

@router.post("/register")
async def register(data: RegisterRequest):
	conn = connect_db()	
	cur = conn.cursor()

	user = get_user(data.username)	
	if user == None:
		insert_user(cur, data)	
		conn.commit()
		conn.close()
		return {"message":"created new account"}

def insert_user(cur: Cursor, data: RegisterRequest):
	if data == None:
		return ValueError("Data was none")

	cur.execute(
		"INSERT INTO users VALUES (?,?,?,?,?,?)",
		(data.id, data.username, data.email, data.password, data.created_at, data.role_id,)
	)

	return cur


@router.get("/user")
async def get_current_user(access_token: str | None = Cookie(default=None)):
	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	payload = decode_payload(access_token)
	return {"id":payload["uid"], "username":payload["username"], "role_id":payload["role_id"]}


# @router.get("/register")
# async def register(data: RegisterRequest):
# 	user: tuple | None = get_user(data.username)
# 	if user == None:
# 		cur.execute(
# 			"INSERT INTO users VALUES (?,?,?,?,?,?)",
# 			(data.id, data.username, data.email, data.password, data.created_at, data.role_id,)
# 		)
# 		conn.commit()
# 		conn.close()
# 
# 		return {"message": "User Created"}
# 	else:
# 		raise HTTPException(status_code=401, detail="Account already exists")
