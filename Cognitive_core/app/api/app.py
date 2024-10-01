from fastapi import FastAPI
from app.api.endpoints.example import router as example_router

app = FastAPI()

app.include_router(example_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Cognitive CORE API"}
