from typing import List, TYPE_CHECKING, Any, TypeVar
from fastapi import status, HTTPException

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


async def get_user_item_by_id(
    entity: Any,
    item_id: int,
    user_id: int,
    session: AsyncSession,
) -> Any:
    item = await session.get(
        entity,
        item_id,
    )
    if item.user_id == user_id:
        return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no such object!",
    )


async def delete_item_by_user_id(
    entity: Any,
    item_id: int,
    user_id: int,
    session: AsyncSession,
) -> dict[str, str]:
    await session.delete(await get_user_item_by_id(entity, item_id, user_id, session))
    await session.commit()
    return {"status_code": status.HTTP_204_NO_CONTENT}
