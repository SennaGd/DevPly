from sqlite3 import Connection, Cursor

from pydantic import BaseModel

from fastapi import Response, HTTPException, APIRouter, Depends, Cookie

# helper functions
from utils.codec import encode_payload
from utils.database import get_user, connect_db
from utils.user import generate_access_token 
from utils.codec import decode_payload, encode_payload

import jwt

router = APIRouter(prefix="/projects", tags=["Project Utils"])


class TaskRequest(BaseModel):
	requirement_id: int
	project_id: int
	title: str
	description: str
	status: int

class RequirementRequest(BaseModel):
	project_id: int
	title: str
	description: str
	status: int = 0

# returns False if item exists else True
def item_exists(cur: Cursor, table: str, row: str, value: str | int):
	item = cur.execute(
		f"SELECT * FROM {table} WHERE {row} = ?",
		(value,)
	).fetchall()
	
	print(item)
	if len(item) <= 0:
		return False
	return True


@router.post("/add/requirement")
async def add_requirement(data: RequirementRequest):
	conn = connect_db()
	cur = conn.cursor()

	if not item_exists(cur, "projects", "id", data.project_id):
		return { "message":"project does not exist" }
	if item_exists(cur, "requirements", "title", data.title):
		return { "message":"requirement already exists" }

	# insert new requirement
	insert = cur.execute(
		"""
		INSERT INTO requirements (project_id, title, description, status) VALUES (?, ?, ?, ?)
		""", 
		(data.project_id, data.title, data.description, data.status, )
	)

	print(insert)
	conn.commit()
	conn.close()

	return {"message":"added new requirement successfully!"}

	
@router.post("/add/tasks")
async def add_tasks(data: TaskRequest):
	conn = connect_db()
	cur = conn.cursor()

	# fetch project
	if not item_exists(cur, "projects", "id", data.project_id):
		return { "message":"project does not exist" }
	if item_exists(cur, "tasks", "title", data.title):
		return { "message":"requirement already exists" }


	insert = cur.execute(
		"""
		INSERT INTO tasks (requirement_id, project_id, title, description, status) VALUES (?, ?, ?, ?, ?)
		""", 
		(data.requirement_id, data.project_id, data.title, data.description, data.status, )
	)

	conn.commit()
	conn.close()

	return {"message":"Added new task successfully!"}


class GetTasksRequest(BaseModel):
	project_id: int

@router.get("get/tasks")
async def fetch_tasks(access_token: str, data: GetTasksRequest):
	conn = connect_db()
	cur = conn.cursor()

	if not access_token:
		return { "message":"not logged in"}
		

	payload = decode_payload(access_token)
	if not item_exists(cur, "users", "id", payload["uid"]):
		...
