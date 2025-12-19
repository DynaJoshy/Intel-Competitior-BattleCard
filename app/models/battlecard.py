from pydantic import BaseModel
from typing import List
from datetime import datetime

class BattleCard(BaseModel):
    id: str
    competitor: str
    summary: str
    strengths: List[str]
    weaknesses: List[str]
    objections: List[str]
    rebuttals: List[str]
    sources: List[str]
    created_at: datetime