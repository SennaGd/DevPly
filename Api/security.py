from typing import Any

from fastapi import Cookie, HTTPException
import jwt

SECRET_KEY = "change-this-to-a-long-random-secret-string"
ALGORITHM = "HS256"


# returns decoded payload
def decode_payload(access_token: str | None = Cookie(None)):
	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try:
		return jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])

	except jwt.ExpiredSignatureError:
		raise HTTPException(status_code=401, detail="Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(status_code=401, detail="Invalid token")

# returns encoded payload
def encode_payload(payload: dict[str, Any]):
	return jwt.encode(payload, SECRET_KEY, ALGORITHM)
