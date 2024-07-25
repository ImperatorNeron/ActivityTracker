from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import database_helper, User, Folder
from src.authentication.dependencies.fastapi_users_routers import current_active_user
from src.core.crud import (
    get_user_item_by_id,
    create_item_by_user_id,
    get_items_by_user_id,
    delete_item_by_user_id,
    update_user_item_by_id,
)
from src.folder.crud import delete_tasks_and_folder
from src.folder.schemas import FolderRead, FolderCreate, FolderUpdate

router = APIRouter(
    prefix="/folders",
    tags=["Folders"],
)


@router.get("/", response_model=List[FolderRead])
async def get_folders(
    current_user: Annotated[
        User,
        Depends(current_active_user),
    ],
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
):
    return await get_items_by_user_id(
        Folder,
        current_user.id,
        session,
    )


@router.post("/", response_model=FolderRead)
async def create_folder(
    folder_in: FolderCreate,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await create_item_by_user_id(
        Folder,
        folder_in,
        current_user.id,
        session,
    )


@router.get("/{current_folder_id}", response_model=FolderRead)
async def get_folder(
    current_folder_id: int,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await get_user_item_by_id(
        Folder, current_folder_id, current_user.id, session
    )


@router.patch("/{current_folder_id}", response_model=FolderRead)
async def update_folder(
    folder_in: FolderUpdate,
    current_folder_id: int,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await update_user_item_by_id(
        Folder,
        current_folder_id,
        folder_in,
        current_user.id,
        session,
    )


@router.delete("/delete-all/{folder_id}")
async def delete_tasks_with_folder(
    folder_id: int,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await delete_tasks_and_folder(folder_id, current_user.id, session)


@router.delete("/delete/{folder_id}")
async def delete_folder(
    folder_id: int,
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
    current_user: Annotated[  # noqa
        User,
        Depends(current_active_user),
    ],
):
    return await delete_item_by_user_id(Folder, folder_id, current_user.id, session)
