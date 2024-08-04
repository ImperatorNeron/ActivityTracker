from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models import TaskTrackerBaseModel
from src.core.mixins import IdIntPkMixin, UserRelationMixin

if TYPE_CHECKING:
    from src.folder.models import Folder
    from src.activity.models import Activity


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
    folder: Mapped["Folder"] = relationship("Folder", back_populates=_back_populates)

    activities: Mapped["Activity"] = relationship("Activity", back_populates="task")

    __table_args__ = (
        CheckConstraint(
            "start_value >= 0 AND goal_value >= 0",
            name="non_negative_values",
        ),
    )
