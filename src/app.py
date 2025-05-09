from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers.prop_API_controller import router as images_router
from src.controllers.base_controller import router as base_router
app = FastAPI(title="Image‑Tagging Service")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(images_router)
app.include_router(base_router)
