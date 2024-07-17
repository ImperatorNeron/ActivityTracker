from fastapi_users.db import SQLAlchemyBaseUserTable

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models import TaskTrackerBaseModel


class User(TaskTrackerBaseModel, SQLAlchemyBaseUserTable[int]):
    nickname: Mapped[str] = mapped_column("nickname", String(100), default="Newbie")