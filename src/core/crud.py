from typing import List, TYPE_CHECKING, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

if TYPE_CHECKING:
    from sqlalchemy import Result
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_items_by_user_id(
    entity: Any, user_id: int, session: AsyncSession
) -> List:
    result: "Result" = await session.execute(
        select(entity).where(entity.user_id == user_id).order_by(entity.id)
    )
    return list(result.scalars().all())


async def create_item_by_user_id(
    entity: Any,
    item_in: Any,
    user_id: int,
    session: AsyncSession,
) -> Any:
    item = entity(**item_in.model_dump(), user_id=user_id)
    session.add(item)
    await session.commit()
    return item
