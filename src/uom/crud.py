from typing import TYPE_CHECKING, List

from sqlalchemy import select

from src.uom.models import UOM
from src.uom.schemas import UOMCreate

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
