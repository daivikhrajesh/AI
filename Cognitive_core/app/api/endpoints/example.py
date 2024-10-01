from fastapi import APIRouter
from app.main.comprehension.comprehension_agent import process_user_input

router = APIRouter()

@router.post("/process/")
async def process(data: str):
    result = process_user_input(data)
    return {"result": result}
