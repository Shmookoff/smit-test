from fastapi import APIRouter, status
from tortoise.contrib.fastapi import HTTPNotFoundError

from .cargo_types.router import cargo_types_router
from .tariffs.router import tariffs_router

api_router = APIRouter(
    prefix="/api", responses={status.HTTP_404_NOT_FOUND: {"model": HTTPNotFoundError}}
)

api_router.include_router(cargo_types_router)
api_router.include_router(tariffs_router)
