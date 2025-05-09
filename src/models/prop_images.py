from pydantic import BaseModel
from typing import List

class Image(BaseModel):
    id: str
    tags: List[str]

class TagUpdate(BaseModel):
    tags: List[str]
