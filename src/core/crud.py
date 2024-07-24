from typing import List, TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

if TYPE_CHECKING:
    from sqlalchemy import Result
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_items_by_user_id(entity, user_id: int, session: AsyncSession) -> List:
    result: "Result" = await session.execute(
        select(entity).where(entity.user_id == user_id).order_by(entity.id)
    )
    return list(result.scalars().all())
