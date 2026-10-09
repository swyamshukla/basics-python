from pydantic import BaseModel


class InputResponse(BaseModel):
    question: str
    words: int