import uuid
from typing import List, Dict

from src.models.prop_images import Image

_images: Dict[str, Image] = {}

def create_image(tags: List[str]) -> Image:
    image_id = str(uuid.uuid4())
    img = Image(id=image_id, tags=tags)
    _images[image_id] = img
    return img

def generate_tags_for_image(content: bytes) -> List[str]:
    # TODO: hook into ML/API
    return ["example_tag", "sample_tag"]