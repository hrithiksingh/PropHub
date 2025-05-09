from pydantic import BaseModel
from typing import List, Dict


class Image(BaseModel):
    id: str
    tags: List[str]

class TagUpdate(BaseModel):
    tags: List[str]

class TagResponse(BaseModel):
    """
    Response schema for image tag generation:
    - mandatory: one chosen tag per category
    - extras: list of additional descriptive tags
    """
    mandatory: Dict[str, str]
    extras: List[str]