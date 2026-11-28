from . import * 
router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/get/all")
async def get_roles():
	conn = connect_db()
	cur = conn.cursor()

	roles = cur.execute(
		"SELECT * FROM roles;"
	)

	return { "message":roles }


