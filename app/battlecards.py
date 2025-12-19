import uuid
from datetime import datetime
from .db import get_conn
from .models import BattleCard

async def save_battlecard(competitor: str, card_json: dict):
    card_id = str(uuid.uuid4())
    bc = BattleCard(id=card_id, competitor=competitor, json=card_json, created_at=str(datetime.utcnow()))

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO battlecards (id, competitor, json, created_at) VALUES (?, ?, ?, ?)",
        (bc.id, bc.competitor, str(bc.json), bc.created_at)
    )
    conn.commit()

    return bc