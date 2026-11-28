from . import *

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
    allow_origins=[
		ADDRESS,
		f"http://127.0.0.1:{WEB_PORT}"
	],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authRouter)
app.include_router(projectsRouter)
app.include_router(userRouter)
app.include_router(roleRouter)
app.include_router(inviteRouter)
