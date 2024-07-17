from typing import TYPE_CHECKING, Annotated
from fastapi import Depends

from src.core.database_helper import database_helper
from src.authentication.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_db(
    session: Annotated[
        "AsyncSession",
        Depends(database_helper.session_getter),
    ],
):
    yield AccessToken.get_db(session)
