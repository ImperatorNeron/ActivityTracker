from typing import TYPE_CHECKING, List
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.mixins import IdIntPkMixin
from src.core.models import TaskTrackerBaseModel

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from src.folder.models import Folder
    from src.task.models import Task


class User(IdIntPkMixin, TaskTrackerBaseModel, SQLAlchemyBaseUserTable[int]):
    nickname: Mapped[str] = mapped_column("nickname", String(100), default="Newbie")
    folders: Mapped[List["Folder"]] = relationship("Folder", back_populates="user")
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
