from openai import OpenAI
from .config import settings
from .embeddings import retrieve

client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def competitor_extractor(text: str):
    prompt = f"""
    Extract competitor company names from the text below. Return JSON list of names.
    Text: {text}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

async def generate_battlecard(competitor: str):
    sources = retrieve(competitor, k=8)
    context = "\n".join([f"{i}: {txt}" for i, txt in sources])

    prompt = f"""
    Using ONLY the context below, create a battle card for competitor {competitor}:
    - 3-sentence summary
    - 3 strengths
    - 3 weaknesses
    - 3 objections + rebuttals
    - 2 CRM quotes with ids

    Context:
    {context}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content, sources