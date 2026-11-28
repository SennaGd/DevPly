from . import *

router = APIRouter(prefix="/invites", tags=["Invites"])

# /invites/get/all
@router.get("/get/all")
async def get_all_invites(access_token: str | None = Cookie(None)):
	conn = connect_db()
	cur = conn.cursor()

	payload = decode_payload(access_token)

	if not access_token:
		return { "message":"not logged in" }
	
	invites = cur.execute("""
		SELECT * FROM invites WHERE user_id = ?
	""", (payload["uid"])).fetchall()

	if len(invites) < 0:
		return { "message":"no invites yet" }
	else:
		return { "message":invites}


class InviteRequest(BaseModel):
	id: int | None = Field(default=None, primary_key=True)
	user_id: int
	project_id: int
	status: str = "awaiting" # expected: awaiting, accepted, declined
	joined_at: str = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
	
# /invites/create
@router.post("/create")
async def create_invite(
		data: InviteRequest, 
		access_token: str | None = Cookie(None)
):

	conn = connect_db()
	cur = conn.cursor()

	# must be logged in
	if not access_token:
		return { "message":"not logged in" }

	# check if user is already invited to project
	check = cur.execute(
			"SELECT * FROM invites WHERE user_id = ? AND project_id = ?", 
			(data.user_id, data.project_id,)
	).fetchall()

	if len(check) > 0:
		return {"message":"user was already invited to project"}

	print(data)	
	# insert query
	cur.execute(
			"INSERT INTO invites (id, user_id, project_id, status, joined_at) VALUES (?, ?, ?, ?, ?)",
			(data.id, data.user_id, data.project_id, data.status, data.joined_at,)
	)

	conn.commit() 
	conn.close()

	return {"message":"invited user"}
	
