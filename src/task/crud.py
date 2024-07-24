from typing import List, TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src import Task
from src.core import crud

if TYPE_CHECKING:
    from sqlalchemy import Result


async def get_tasks(user_id: int, session: AsyncSession) -> List["Task"]:
    return await crud.get_items_by_user_id(Task, user_id, session)
