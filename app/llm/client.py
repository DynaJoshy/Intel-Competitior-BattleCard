from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def chat(messages, model="gpt-4o"):
    return client.chat.completions.create(
        model=model,
        messages=messages
    ).choices[0].message.content