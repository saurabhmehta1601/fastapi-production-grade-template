# This module provides method `create_app` that provides fresh instance of app.
# This is particularly useful for getting app for testing (each test can run app from scratch ) and configuration.
# In production we will need only single instance.

from fastapi import FastAPI
from app.api.router import router as api_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app
