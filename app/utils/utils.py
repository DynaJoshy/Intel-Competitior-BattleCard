from typing import List, Dict
import hashlib


def _hash_text(text: str) -> str:
    """Stable hash for chunk IDs (prevents duplicates across runs)."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:12]


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100,
    min_length: int = 50
) -> List[Dict]:
    """
    Splits text into overlapping chunks.
    Returns a list of dicts:
    {
        id: str,
        text: str,
        start_token: int,
        end_token: int
    }
    """
    tokens = text.split()
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]

        if len(chunk_tokens) < min_length:
            break

        chunk_text = " ".join(chunk_tokens)
        chunk_id = _hash_text(chunk_text)

        chunks.append({
            "id": chunk_id,
            "text": chunk_text,
            "start_token": start,
            "end_token": min(end, len(tokens))
        })

        start = end - overlap
        if start < 0:
            start = 0

    return chunks
