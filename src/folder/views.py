from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import database_helper, User
from src.authentication.dependencies.fastapi_users_routers import current_active_user
from src.folder import crud
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
    return await crud.get_folders(current_user.id, session)


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
    return await crud.create_folder(
        folder_in,
        current_user.id,
        session,
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
    return await crud.update_folder(
        current_folder_id,
        folder_in,
        current_user.id,
        session,
    )
