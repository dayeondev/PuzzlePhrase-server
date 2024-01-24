from openai import AsyncOpenAI

from app.core.config import settings

async def get_openai_client():
    return AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
