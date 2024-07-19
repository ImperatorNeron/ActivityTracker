from typing import List, TYPE_CHECKING

from sqlalchemy import select
from src.folder.models import Folder

if TYPE_CHECKING:
    from sqlalchemy import Result
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_folders(user_id: int, session: "AsyncSession") -> List[Folder]:
    result: "Result" = await session.execute(
        select(Folder).where(Folder.user_id == user_id).order_by(Folder.title),
    )
    return list(result.scalars().all())
