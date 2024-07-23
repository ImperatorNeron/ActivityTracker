from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import TaskTrackerBaseModel
from src.core.mixins import UserRelationMixin, IdIntPkMixin

if TYPE_CHECKING:
    from src.task.models import Task


class Folder(TaskTrackerBaseModel, UserRelationMixin, IdIntPkMixin):
    _back_populates = "folders"

    title: Mapped[str] = mapped_column("title", String(100), unique=True)
    description: Mapped[str] = mapped_column("description", nullable=True)
    tasks_quantity: Mapped[int] = mapped_column(
        "tasks_quantity", default=0, server_default="0"
    )
    creation_date: Mapped[datetime] = mapped_column(
        "creation_date",
        default=datetime.utcnow(),
        server_default=f"{datetime.utcnow()}",
    )
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="folder")

    __table_args__ = (
        CheckConstraint(
            tasks_quantity >= 0,
            name="check_tasks_quantity_non_negative",
        ),
    )
