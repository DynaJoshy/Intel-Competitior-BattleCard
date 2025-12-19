from app.services.embedding_service import retrieve_chunks

async def retrieve_context(competitor: str, k: int = 8) -> list[tuple[str, str]]:
    """Returns list of (chunk_id, text)"""
    return retrieve_chunks(competitor, k=k)