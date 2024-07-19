from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import database_helper, User
from src.authentication.dependencies.fastapi_users_routers import current_active_user
from src.folder import crud
from src.folder.schemas import FolderRead

router = APIRouter(
    prefix="/folders",
    tags=["Folders"],
)


@router.get("/", response_model=List[FolderRead])
async def get_folders(
    user: Annotated[
        User,
        Depends(current_active_user),
    ],
    session: Annotated[
        AsyncSession,
        Depends(database_helper.session_getter),
    ],
):
    return await crud.get_folders(user.id, session)
