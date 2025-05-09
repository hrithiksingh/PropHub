from typing import List, Dict

from src.models.prop_images import Image

_images: Dict[str, Image] = {}

def update_tags(image_id: str, tags: List[str]) -> Image:
    img = _images.get(image_id)
    if img:
        img.tags = tags
    return img