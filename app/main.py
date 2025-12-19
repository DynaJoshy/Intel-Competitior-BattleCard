from fastapi import FastAPI
from .db import init_db
from .ingest import ingest_deal
from .agents import competitor_extractor, generate_battlecard
from .battlecards import save_battlecard
import json

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.post("/ingest")
async def ingest(raw_text: str, crm_id: str):
    return await ingest_deal(raw_text, crm_id)

@app.post("/battlecard")
async def battlecard(competitor: str):
    card, sources = await generate_battlecard(competitor)
    bc = await save_battlecard(competitor, {"card": card, "sources": sources})
    return bc