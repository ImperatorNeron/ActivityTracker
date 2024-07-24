from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import User, Task
from src.authentication.dependencies.fastapi_users_routers import current_active_user
from src.core.crud import (
    get_user_item_by_id,
    delete_item_by_user_id,
    create_item_by_user_id,
    get_items_by_user_id,
    update_user_item_by_id,
)
from src.core.database_helper import database_helper
from src.task.schemas import ReadTask, CreateTask, UpdateTask

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
    return await get_items_by_user_id(Task, current_user.id, session)


@router.post("/create", response_model=ReadTask)
async def create_task(
    task_in: CreateTask,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await create_item_by_user_id(Task, task_in, current_user.id, session)


@router.get("/{task_id}", response_model=ReadTask)
async def get_task_by_id(
    task_id: int,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await get_user_item_by_id(Task, task_id, current_user.id, session)


@router.patch("/{task_id}", response_model=ReadTask)
async def update_task(
    task_id: int,
    task_in: UpdateTask,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await update_user_item_by_id(
        Task, task_id, task_in, current_user.id, session
    )


@router.delete("/delete/{task_id}")
async def delete_task(
    current_task_id: int,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await delete_item_by_user_id(
        Task,
        current_task_id,
        current_user.id,
        session,
    )
