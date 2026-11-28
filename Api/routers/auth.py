# authentication endpoints 
from . import *

router = APIRouter(prefix="/auth", tags=["Auth"])

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

# /auth/register
@router.post("/register")
async def register(data: RegisterRequest):
	conn = connect_db()	
	cur = conn.cursor()

	user = get_user(data.username)	
	if user == None:
		cur.execute(
			"INSERT INTO users (id, username, email, password, created_at, role_id) VALUES (?,?,?,?,?,?);",
			(data.id, data.username, data.email, data.password, data.created_at, data.role_id,)
		)


		conn.commit()
		conn.close()
		return {"message":"created new account"}

