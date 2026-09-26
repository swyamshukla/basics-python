
from pydantic import BaseModel

class ChatModel(BaseModel):
    prompt: str
