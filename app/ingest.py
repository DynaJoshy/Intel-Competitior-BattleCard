import uuid
from datetime import datetime
from .db import get_conn
from .models import Deal

async def ingest_deal(raw_text: str, crm_id: str):
    deal_id = str(uuid.uuid4())
    deal = Deal(id=deal_id, crm_id=crm_id, raw_text=raw_text, created_at=str(datetime.utcnow()))

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO deals (id, crm_id, raw_text, created_at) VALUES (?, ?, ?, ?)",
        (deal.id, deal.crm_id, deal.raw_text, deal.created_at)
    )
    conn.commit()

    return deal