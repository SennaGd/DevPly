from . import *

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
