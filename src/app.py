from fastapi import FastAPI
from .controllers.prop_API_controller import router as images_router

app = FastAPI(title="Image‑Tagging Service")

app.include_router(images_router)
