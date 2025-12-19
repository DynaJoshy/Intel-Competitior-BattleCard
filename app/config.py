import os

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    DB_PATH = os.getenv("DB_PATH", "db.sqlite")

settings = Settings()