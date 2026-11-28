from datetime import datetime, timedelta, timezone
from fastapi import Cookie, HTTPException
from dotenv import load_dotenv
from pathlib import Path
from typing import Any

import jwt, sqlite3, os
