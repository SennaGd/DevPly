from datetime import datetime, timezone, timedelta
from pydantic import BaseModel
from sqlmodel import Field

class ProjectRequest(BaseModel):
	id: int | None = Field(default=None, primary_key=True)
	title: str
	description: str
	creator_id: int	
	created_at: str = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

class FetchProjectRequest(BaseModel):
	project_id: str 


