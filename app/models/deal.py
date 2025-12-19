from pydantic import BaseModel
from datetime import datetime

class Deal(BaseModel):
    id: str
    crm_id: str
    raw_text: str
    created_at: datetime