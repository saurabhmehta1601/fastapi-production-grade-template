from fastapi import APIRouter
from app.api.v1.endpoints.books import router as books_router

router = APIRouter(prefix="/v1")

router.include_router(books_router)
