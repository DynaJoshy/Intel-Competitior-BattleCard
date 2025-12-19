from app.llm.client import chat
from app.llm.prompts import GENERATE_BATTLECARD

async def generate_battlecard(competitor: str, sources: list[tuple[str, str]]) -> str:
    context = "".join([f"[{cid}] {text}" for cid, text in sources])

    return chat([
        {
            "role": "user",
            "content": GENERATE_BATTLECARD.format(
                competitor=competitor,
                context=context
            )
        }
    ])