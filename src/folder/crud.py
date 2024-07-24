from typing import List, TYPE_CHECKING, Optional

from fastapi import HTTPException
from fastapi import status

from src.core import crud
from src.core.crud import create_item_by_user_id
from src.folder.models import Folder
from src.folder.schemas import FolderCreate, FolderUpdate

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_folders(user_id: int, session: "AsyncSession") -> List[Folder]:
    return await crud.get_items_by_user_id(Folder, user_id, session)


async def create_folder(
    folder_in: FolderCreate,
    user_id: int,
    session: "AsyncSession",
) -> Folder:
    return await create_item_by_user_id(Folder, folder_in, user_id, session)


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
