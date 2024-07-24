from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from src import Task
from src.core import crud
from src.task.schemas import CreateTask


async def get_tasks(user_id: int, session: AsyncSession) -> List["Task"]:
    return await crud.get_items_by_user_id(Task, user_id, session)


async def create_task(
    task_in: CreateTask,
    user_id: int,
    session: AsyncSession,
) -> Task:
    task = Task(**task_in.model_dump(), user_id=user_id)
    session.add(task)
    await session.commit()
    return task
