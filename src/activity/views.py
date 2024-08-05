from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src import User
from src.activity import crud
from src.activity.schemas import ActivityRead, ActivityCreate
from src.authentication.dependencies.fastapi_users_routers import current_active_user
from src.core.database_helper import database_helper


router = APIRouter(
    prefix="/activity",
    tags=["Activities"],
)


@router.get("/{task_id}", response_model=List[ActivityRead])
async def get_user_task_activity(
    task_id: int,
    current_user: Annotated[
        User,
        Depends(current_active_user),
    ],
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
):
    return await crud.get_user_task_activity(task_id, current_user.id, session)


@router.post("/{task_id}", response_model=ActivityRead)
async def add_activity(
    activity_in: ActivityCreate,
    current_user: Annotated[
        User,
        Depends(current_active_user),
    ],
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
):
    return await crud.add_activity(activity_in, current_user.id, session)

