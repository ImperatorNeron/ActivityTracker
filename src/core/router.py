from fastapi import APIRouter
from src.core.settings import settings

router = APIRouter(prefix=settings.api_version_prefix)
