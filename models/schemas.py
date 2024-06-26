from pydantic import BaseModel

class TextPrompt(BaseModel):
    prompt: str
