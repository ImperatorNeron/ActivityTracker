from datetime import datetime

from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src import TaskTrackerBaseModel
from src.core.mixins import UserRelationMixin


class Folder(TaskTrackerBaseModel, UserRelationMixin):
    _back_populates = "folders"
    _primary_key = True

    title: Mapped[str] = mapped_column("title", String(100), primary_key=True)
    description: Mapped[str] = mapped_column("description", nullable=True)
    tasks_quantity: Mapped[int] = mapped_column("tasks_quantity", default=0, server_default="0")
    creation_date: Mapped[datetime] = mapped_column(
        "creation_date", default=datetime.utcnow(), server_default=f"{datetime.utcnow()}"
    )

    __table_args__ = (
        CheckConstraint(
            tasks_quantity >= 0,
            name="check_tasks_quantity_non_negative",
        ),
    )
