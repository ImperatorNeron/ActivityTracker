from datetime import datetime

from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import TaskTrackerBaseModel
from src.core.mixins import IdIntPkMixin, UserRelationMixin


class Task(TaskTrackerBaseModel, UserRelationMixin, IdIntPkMixin):
    _back_populates = "tasks"

    title: Mapped[str] = mapped_column("title", String(100), unique=True)
    description: Mapped[str] = mapped_column("description", nullable=True)
    creation_date: Mapped[datetime] = mapped_column(
        "creation_date",
        default=datetime.utcnow(),
        server_default=f"{datetime.utcnow()}",
    )
    start_value: Mapped[float] = mapped_column(
        "start_value",
        default=0,
        server_default="0",
    )
    goal_value: Mapped[float] = mapped_column("goal_value")
    start_date: Mapped[datetime] = mapped_column("start_date", nullable=True)
    finish_date: Mapped[datetime] = mapped_column("finish_date", nullable=True)

    folder_id: Mapped[int] = mapped_column(ForeignKey("folders.id"), nullable=True)
    folder = relationship("Folder", _back_populates)

    __table_args__ = (
        CheckConstraint(
            "start_value >= 0 AND goal_value >= 0",
            name="non_negative_values",
        ),
    )
