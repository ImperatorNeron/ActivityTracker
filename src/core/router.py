from fastapi import APIRouter
from src.core.settings import settings
from src.authentication.views import router as auth_router

router = APIRouter(prefix=settings.api_version_prefix)

router.include_router(auth_router)
