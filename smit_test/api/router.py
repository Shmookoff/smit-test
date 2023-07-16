from fastapi import APIRouter

from .tariffs import tariffs_router

api_router = APIRouter(prefix="api")

api_router.include_router(tariffs_router)
