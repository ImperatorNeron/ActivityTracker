from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy


from src.authentication.dependencies.access_tokens import get_access_token_db
from src.core.settings import settings

if TYPE_CHECKING:
    from src.authentication.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_token_db),
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
