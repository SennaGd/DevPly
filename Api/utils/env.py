from . import *

ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"

load_dotenv(ENV_PATH)

WEB_ADDR = os.getenv("WEB_ADDR")
WEB_PORT = os.getenv("WEB_PORT")
ADDRESS = str(f"{WEB_ADDR}:{WEB_PORT}")

print(ENV_PATH, ADDRESS)
