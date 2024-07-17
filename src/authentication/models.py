from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
    SQLAlchemyAccessTokenDatabase,
)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped
from src import TaskTrackerBaseModel

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(TaskTrackerBaseModel, SQLAlchemyBaseAccessTokenTable[int]):
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyAccessTokenDatabase(session, cls)
