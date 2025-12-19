from fastapi import APIRouter, HTTPException
from app.services.battlecard_service import create_battlecard

router = APIRouter()

@router.post("/battlecards/{competitor}")
async def generate(competitor: str):
    try:
        return await create_battlecard(competitor)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))