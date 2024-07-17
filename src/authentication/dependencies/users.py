from typing import TYPE_CHECKING, Annotated
from fastapi import Depends

from src.core.database_helper import database_helper
from src.user.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated[
        "AsyncSession",
        Depends(database_helper.session_getter),
    ],
):
    yield User.get_db(session)
