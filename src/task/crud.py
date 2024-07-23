from typing import List, TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src import Task

if TYPE_CHECKING:
    from sqlalchemy import Result


async def get_tasks(user_id: int, session: AsyncSession) -> List["Task"]:
    result: "Result" = await session.execute(
        select(Task).where(Task.user_id == user_id).order_by(Task.id)
    )
    return list(result.scalars().all())
