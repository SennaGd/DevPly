from sqlite3 import Connection, Cursor
import jwt
from pydantic import BaseModel

from fastapi import ( 
	Cookie, 
	Depends,

	Response, 
	HTTPException, 
	APIRouter, 
)

# helper functions
from ..utils.codec import decode_payload, encode_payload
from ..utils.database import get_user, connect_db
from ..utils.user import generate_access_token 

# dataclasses/models
from .dataclasses.project_classes import	( 
	ProjectRequest, 
	FetchProjectRequest,
)

from .dataclasses.auth_classes import (
	LoginRequest, 
	RegisterRequest,
)

from .dataclasses.requirements_classes import *
from .dataclasses.tests_classes import *
