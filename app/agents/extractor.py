from app.llm.client import chat
from app.llm.prompts import EXTRACT_COMPETITORS
import json

async def extract_competitors(raw_text: str) -> list[str]:
    response = chat([
        {"role": "user", "content": EXTRACT_COMPETITORS.format(text=raw_text)}
    ], model="gpt-4o-mini")

    try:
        competitors = json.loads(response)
        return [c.strip() for c in competitors if c.strip()]
    except Exception:
        return []