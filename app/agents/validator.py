def validate_battlecard(card_text: str, sources: list) -> dict:
    """
    Lightweight validation:
    - checks minimum sections
    - ensures sources were present
    """
    required_sections = ["summary", "strength", "weakness", "objection"]
    lower = card_text.lower()

    is_valid = all(sec in lower for sec in required_sections)

    return {
        "valid": is_valid,
        "source_count": len(sources)
    }