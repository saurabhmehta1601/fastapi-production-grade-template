from fastapi import APIRouter
from .endpoints.users import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(user_router)