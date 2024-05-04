from fastapi import FastAPI
from .routes.endpoints import router as api_router

app = FastAPI(title='Cleric Project')

app.include_router(api_router)

print(":: inside main.py ::")