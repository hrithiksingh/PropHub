from fastapi import APIRouter, status

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