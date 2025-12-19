from pydantic import BaseModel
from typing import List

class Deal(BaseModel):
    id: str
    crm_id: str
    raw_text: str
    created_at: str

class BattleCard(BaseModel):
    id: str
    competitor: str
    json: dict
    created_at: str