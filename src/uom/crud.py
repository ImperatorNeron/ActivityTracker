from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import select

from src.uom.models import UOM
from src.uom.schemas import UOMCreate, UOMPartialUpdate

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from sqlalchemy import Result


async def uom_list(session: "AsyncSession") -> List[UOM]:
    result: "Result" = await session.execute(
        select(UOM).order_by(UOM.id),
    )
    return list(result.scalars().all())


async def add_uom(uom: UOMCreate, session: "AsyncSession") -> UOM:
    new_uom = UOM(**uom.model_dump())
    session.add(new_uom)
    await session.commit()
    return new_uom


async def partial_update_uom(
    uom_in: UOMPartialUpdate,
    uom_now_id: int,
    session: "AsyncSession",
) -> UOM:
    uom = await get_uom(uom_now_id, session)
    for key, value in uom_in.model_dump(exclude_unset=True).items():
        setattr(uom, key, value)
    await session.commit()
    return uom


async def get_uom(uom_id: int, session: "AsyncSession") -> Optional[UOM]:
    return await session.get(UOM, uom_id)
