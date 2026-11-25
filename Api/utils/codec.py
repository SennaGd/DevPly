from typing import Any

from fastapi import Cookie, HTTPException
import jwt

SECRET_KEY = "change-this-to-a-long-random-secret-string"
ALGORITHM = "HS256"



def decode_payload(access_token: str | None = Cookie(None)) -> dict[str, Any]:
	if not access_token:
		raise HTTPException(401, "Not logged in")

	return jwt.decode(access_token, SECRET_KEY, ALGORITHM)


def encode_payload(payload: dict[str, Any]) -> str:
	return jwt.encode(payload, SECRET_KEY, ALGORITHM)

