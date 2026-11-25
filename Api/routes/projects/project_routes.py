from sqlite3 import Connection, Cursor

from pydantic import BaseModel

from .project_models import ( FetchProjectRequest, ProjectRequest )
from fastapi import Response, HTTPException, APIRouter, Depends, Cookie

# helper functions
from utils.codec import encode_payload
from utils.database import get_user, connect_db
from utils.user import generate_access_token 
from utils.codec import decode_payload, encode_payload

import jwt
router = APIRouter(prefix="/projects", tags=["Project"])

@router.post("/create")
async def create_project(projectData: ProjectRequest):
	conn = connect_db()
	cur = conn.cursor()

	project = cur.execute(
			"SELECT * FROM projects WHERE title = ?",
			(projectData.title,)
		).fetchone()

	if project != None:
		return {"message":"project already exists"}

	cur.execute(
			"""
            INSERT INTO projects (title, description, creator_id, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                projectData.title,
                projectData.description,
                projectData.creator_id,
                projectData.created_at,
            ),
		)
	conn.commit()
	conn.close()

	return {"message":"Created new project successfully!"}

@router.get("/fetch_all")
async def fetch_user_projects(access_token: str | None = Cookie(None)):
	conn = connect_db()
	cur = conn.cursor()

	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try: 
		payload = decode_payload(access_token)
		userId = payload["uid"]	

		projects = cur.execute(
				"SELECT * FROM projects WHERE creator_id = ?", (userId,)
		).fetchall()

		return {"message":projects}
	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")

@router.post("/fetch_one")
async def fetch_one_project(project: FetchProjectRequest, access_token: str | None = Cookie(None)):
	conn = connect_db()
	cur = conn.cursor()

	if not access_token:
		raise HTTPException(status_code=401, detail="Not logged in")

	try:
		payload = decode_payload(access_token)
		userId = payload["uid"]
		if project.project_id != None:
			project_id = project.project_id
		project = cur.execute("""
			SELECT * FROM projects WHERE id = ? and creator_id = ?; 
		""", (project.project_id, userId)).fetchone()
		
		
		if project == "None":
			return {"message":"No access"}
		else:
			return {"message":project}
	except jwt.ExpiredSignatureError:
		raise HTTPException(401, "Session expired, please log in again")

	except jwt.InvalidTokenError:
		raise HTTPException(401, "Invalid token")


class ProjectUsersRequest(BaseModel):
	project_id: str

@router.post("/users")
async def fetch_all_users(project: ProjectUsersRequest, access_token: str | None = Cookie(None)):
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
