from typing import List, TYPE_CHECKING, Optional

from fastapi import HTTPException
from sqlalchemy import select
from fastapi import status
from src.folder.models import Folder
from src.folder.schemas import FolderCreate, FolderUpdate

if TYPE_CHECKING:
    from sqlalchemy import Result
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_folders(user_id: int, session: "AsyncSession") -> List[Folder]:
    result: "Result" = await session.execute(
        select(Folder).where(Folder.user_id == user_id).order_by(Folder.title),
    )
    return list(result.scalars().all())


async def create_folder(
    folder_in: FolderCreate,
    user_id: int,
    session: "AsyncSession",
) -> Folder:
    folder = Folder(**folder_in.model_dump(), user_id=user_id)
    session.add(folder)
    await session.commit()
    return folder


async def update_folder(
    current_folder_id: int,
    upd_folder: FolderUpdate,
    user_id: int,
    session: "AsyncSession",
):
    current_folder = await get_folder_by_id(current_folder_id, user_id, session)
    # exclude_unset for removing such things: title=None, time=None
    for key, value in upd_folder.model_dump(exclude_unset=True).items():
        setattr(current_folder, key, value)
    await session.commit()
    return current_folder


async def get_folder_by_id(
    current_folder_id: int,
    user_id: int,
    session: "AsyncSession",
) -> Optional[Folder]:
    folder = await session.get(
        Folder,
        current_folder_id,
    )
    if folder.user_id == user_id:
        return folder
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"You don`t have such folder!",
    )
