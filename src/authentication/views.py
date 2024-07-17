from fastapi import APIRouter

from src.authentication.dependencies.backend import authentication_backend
from src.authentication.dependencies.fastapi_users_routers import fastapi_users_routers

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(
    router=fastapi_users_routers.get_auth_router(authentication_backend),
)