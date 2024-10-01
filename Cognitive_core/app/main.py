from fastapi import FastAPI
from app.api.app import app as api_app

app = FastAPI(title="Cognitive CORE", version="1.0")

@app.on_event("startup")
async def startup_event():
    # Startup logic, e.g., loading models or resources
    print("Cognitive CORE is starting up...")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Cognitive CORE API"}

@app.get("/health/")
async def health_check():
    return {"status": "healthy"}
