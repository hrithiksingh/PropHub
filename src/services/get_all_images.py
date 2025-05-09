from typing import List, Dict

from src.models.prop_images import Image

_images: Dict[str, Image] = {}

def get_image(image_id: str) -> Image:
    return _images.get(image_id)

def get_all_images() -> List[Image]:
    return list(_images.values())