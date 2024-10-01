from fastapi import APIRouter
from app.main import process_user_input

router = APIRouter()

@router.post("/process/")
async def process_input(input_data: dict):
    user_input = input_data.get("data", "")
    result = process_user_input(user_input)
    return {"evaluation_result": result}
