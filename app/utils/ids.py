import uuid
import re
import hashlib

# ---------------------------------
# Generic UUIDs (entities)
# ---------------------------------

def new_uuid() -> str:
    """
    Generate a random UUID string.
    Used for deals, battle cards, requests, etc.
    """
    return str(uuid.uuid4())


# ---------------------------------
# Deterministic hashes (content)
# ---------------------------------

def stable_hash(value: str, length: int = 12) -> str:
    """
    Deterministic hash for text-based entities.
    Same input → same output.
    """
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:length]


# ---------------------------------
# Competitor normalization
# ---------------------------------

def normalize_competitor_name(name: str) -> str:
    """
    Normalize competitor names so variants map to one identity.

    Examples:
    - "SFDC" → "salesforce"
    - "Salesforce.com" → "salesforce"
    """
    name = name.lower().strip()
    name = re.sub(r"\.com$", "", name)
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", " ", name)
    return name


def competitor_id(name: str) -> str:
    """
    Stable competitor ID derived from normalized name.
    """
    normalized = normalize_competitor_name(name)
    return f"comp_{stable_hash(normalized)}"


# ---------------------------------
# Chunk IDs (semantic units)
# ---------------------------------

def chunk_id(deal_id: str, chunk_text: str) -> str:
    """
    Deterministic chunk ID.
    Same deal + same text → same ID.
    """
    base = f"{deal_id}:{chunk_text}"
    return f"chk_{stable_hash(base)}"
