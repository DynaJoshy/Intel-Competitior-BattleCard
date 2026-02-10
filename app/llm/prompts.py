EXTRACT_COMPETITORS = """
Extract competitor names from the text below.
Current date and time: {timestamp}
Return JSON array only.
Text: {text}
"""

GENERATE_BATTLECARD = """
Using ONLY the provided context, generate a battle card for {competitor}.
Include summary, strengths, weaknesses, objections, rebuttals.
Cite sources.
Current date and time: {timestamp}
Context:
{context}
"""
