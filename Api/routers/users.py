# endpoints for user queries
from . import *

router = APIRouter(prefix="/users", tags=["Project"])
class ProjectUsersRequest(BaseModel):
	project_id: str

# /users/get/all
@router.post("/get/users")
async def fetch_projects_users(project: ProjectUsersRequest, access_token: str | None = Cookie(None)):
	if not access_token:
		raise HTTPException(401, "Not logged in")

	if project.project_id != None:
		project_id = project.project_id
	
	try:
		payload = decode_payload(access_token)
		user_id = payload["uid"]
	
	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")

# /users/info
@router.get("/info")
async def get_user_info(access_token: str | None = Cookie(default=None)):
	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try:
		payload = decode_payload(access_token)
		return {"id":payload["uid"], "username":payload["username"], "role_id":payload["role_id"]}

	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")
	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")
