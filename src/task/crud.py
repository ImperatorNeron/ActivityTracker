from sqlalchemy.ext.asyncio import AsyncSession

from src import Folder, Task
from src.core.crud import get_user_item_by_id, create_item_by_user_id, update_user_item_by_id
from src.task.schemas import CreateTask, UpdateTask


async def create_task(
    task_in: CreateTask,
    user_id: int,
    session: AsyncSession,
) -> Task:
    if task_in.folder_id is not None:
        await get_user_item_by_id(Folder, task_in.folder_id, user_id, session)
    return await create_item_by_user_id(Task, task_in, user_id, session)


async def update_task(
    task_id: int,
    task_in: UpdateTask,
    user_id: int,
    session: AsyncSession,
) -> Task:
    if task_in.folder_id:
        await get_user_item_by_id(Folder, task_in.folder_id, user_id, session)
    return await update_user_item_by_id(Task, task_id, task_in, user_id, session)
