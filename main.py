from fastapi import FastAPI
from router.user_router import router as user_router  # Sahi tarika

app = FastAPI()

app.include_router(user_router)
