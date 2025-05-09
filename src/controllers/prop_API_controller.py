from fastapi import APIRouter, UploadFile, File, HTTPException,status
from typing import List

from src.models.prop_images import Image, TagUpdate
from src.services.get_all_images import get_image
from src.services.edit_tags import update_tags
from src.services.save_new_image import create_image, generate_tags_for_image

router = APIRouter(prefix="/images", tags=["images"])

@router.get("/", response_model=List[Image])
async def get_all_images():
    return []

@router.post("/analyze", response_model=Image)
async def analyze_image(file: UploadFile = File(...)):
    content = await file.read()
    tags = generate_tags_for_image(content)
    return create_image(tags)

@router.put("/{image_id}/tags", response_model=Image)
async def edit_image_tags(image_id: str, payload: TagUpdate):
    img = get_image(image_id)
    if not img:
        raise HTTPException(404, "Image not found")
    return update_tags(image_id, payload.tags)

router = APIRouter()

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    tags=["health"],
    summary="Service health check"
)
async def health_check():
    """
    Simple endpoint to verify that the service is up.
    """
    return {"message": "ALL is well!"}