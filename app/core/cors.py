from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings, Settings

def setup_cors_middleware(app: FastAPI):

    settings: Settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_credentials=True,
        allow_headers=["*"],
        allow_methods=["GET", "POST"]
    )