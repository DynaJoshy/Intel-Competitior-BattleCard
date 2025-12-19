import uuid
from datetime import datetime
from app.agents.generator import generate_battlecard
from app.agents.validator import validate_battlecard
from app.services.retrieval_service import retrieve_context
from app.db import get_conn

async def create_battlecard(competitor: str):
    sources = await retrieve_context(competitor)

    if not sources:
        raise ValueError("No relevant CRM context found")

    card_text = await generate_battlecard(competitor, sources)
    validation = validate_battlecard(card_text, sources)

    card_id = str(uuid.uuid4())

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO battlecards (id, competitor, json, created_at) VALUES (?, ?, ?, ?)",
        (
            card_id,
            competitor,
            card_text,
            datetime.utcnow().isoformat()
        )
    )
    conn.commit()

    return {
        "id": card_id,
        "competitor": competitor,
        "battlecard": card_text,
        "validation": validation,
        "sources": [cid for cid, _ in sources]
    }