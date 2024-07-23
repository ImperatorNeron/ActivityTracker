from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import User
from src.authentication.dependencies.fastapi_users_routers import current_active_user
from src.core.database_helper import database_helper
from src.task import crud
from src.task.schemas import ReadTask

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("/", response_model=List[ReadTask])
async def get_tasks(
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await crud.get_tasks(current_user.id, session)
