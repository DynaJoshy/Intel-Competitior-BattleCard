from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict

class Deal(BaseModel):
    id: str
    crm_id: str
    raw_text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class BattleCard(BaseModel):
    id: str
    competitor: str
    json: Dict
    created_at: datetime = Field(default_factory=datetime.utcnow)
