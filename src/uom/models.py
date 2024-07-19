from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src import TaskTrackerBaseModel
from src.core.mixins import IdIntPkMixin


class UOM(IdIntPkMixin, TaskTrackerBaseModel):
    short_title: Mapped[str] = mapped_column("short_title", String(10), unique=True)
    full_title: Mapped[str] = mapped_column("full_title", String(100), unique=True)
