from typing import List
from fastapi import APIRouter, Depends
from openai import AsyncOpenAI

from app.api import deps


router = APIRouter()


from pydantic import BaseModel
from typing import List

# 요청 데이터를 위한 Pydantic 모델
class GenerateSentenceRequest(BaseModel):
    words: List[str]

# 응답 데이터를 위한 Pydantic 모델
class GenerateSentenceResponse(BaseModel):
    status: str
    sentence: str


@router.post("/sentence", response_model=GenerateSentenceResponse)
async def generate_sentence(
    # words: List[str],
    request: GenerateSentenceRequest,
    client: AsyncOpenAI = Depends(deps.get_openai_client)
):
    words = ",".join(request.words)
    completion = await client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {
                "role": "system",
                "content": "You are an English teacher.\nI will provide some words. Please create an English sentence based on these words."
            },
            {
                "role": "user",
                "content": f"{words}"
            },
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0.2
    )
    # get content from completion
    content = completion.choices[0].message.content

    

    return GenerateSentenceResponse(status="success", sentence=content)
