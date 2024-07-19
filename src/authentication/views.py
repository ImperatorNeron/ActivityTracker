from fastapi import APIRouter

from src.authentication.dependencies.backend import authentication_backend
from src.authentication.dependencies.fastapi_users_routers import fastapi_users_routers
from src.user.schemas import UserRead, UserCreate

router = APIRouter(prefix="/auth", tags=["Auth"])

router.include_router(
    router=fastapi_users_routers.get_auth_router(authentication_backend),
)

router.include_router(
    router=fastapi_users_routers.get_register_router(UserRead, UserCreate),
)

router.include_router(
    router=fastapi_users_routers.get_verify_router(UserRead)
)
