from typing import TYPE_CHECKING
from src.core import crud
from src.folder.models import Folder
from src.folder.schemas import FolderUpdate

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def update_folder(
    current_folder_id: int,
    upd_folder: FolderUpdate,
    user_id: int,
    session: "AsyncSession",
):
    current_folder = await crud.get_user_item_by_id(
        Folder,
        current_folder_id,
        user_id,
        session,
    )

    # exclude_unset for removing such things: title=None, time=None
    for key, value in upd_folder.model_dump(exclude_unset=True).items():
        setattr(current_folder, key, value)
    await session.commit()
    return current_folder
