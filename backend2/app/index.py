from fastapi import FastAPI
from app.routes.routes import charge

app = FastAPI()

app.include_router(charge)