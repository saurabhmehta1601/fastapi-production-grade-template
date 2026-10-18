# This module provides method `create_app` that provides fresh instance of app.
# This is particularly useful for getting app for testing (each test can run app from scratch ) and configuration.
# In production we will need only single instance.

from fastapi import FastAPI
from app.api.router import router as api_router
from app.core.logging import configure_logging
from app.core.cors import setup_cors_middleware
from app.core.middleware import RequestLoggingMiddleware


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    setup_cors_middleware(app)
    app.include_router(api_router)
    return app
