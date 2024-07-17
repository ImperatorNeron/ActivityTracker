from typing import TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.core.models import TaskTrackerBaseModel

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(TaskTrackerBaseModel, SQLAlchemyBaseUserTable[int]):
    nickname: Mapped[str] = mapped_column("nickname", String(100), default="Newbie")

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
