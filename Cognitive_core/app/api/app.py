from fastapi import FastAPI
from main.main import process_user_input
from app.api.endpoints.example import router as example_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Cognitive CORE API"}

@app.post("/process/")
async def process(input: dict):
    result = process_user_input(input["data"])
    return {"evaluation": result}

# Include the example router
app.include_router(example_router)
