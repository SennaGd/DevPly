from datetime import datetime, timedelta, timezone
from typing import Any

from .database import connect_db
def generate_access_token(user: tuple) -> dict[str, Any]:
	return {
		"uid": str(user[0]), 
		"username":user[1], 
		"role_id":user[5], 
		"exp":datetime.now(timezone.utc) + timedelta(hours=24)
	}
