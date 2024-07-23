from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from src.core.settings import settings
from src.authentication.views import router as auth_router
from src.user.views import router as users_router
from src.uom.views import router as uom_router
from src.folder.views import router as folder_router
from src.task.views import router as task_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api_version_prefix, dependencies=[Depends(http_bearer)]
)

router.include_router(auth_router)
router.include_router(users_router)
router.include_router(uom_router)
router.include_router(folder_router)
router.include_router(task_router)
