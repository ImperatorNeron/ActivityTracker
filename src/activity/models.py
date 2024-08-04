from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.core.models import TaskTrackerBaseModel
from src.core.mixins import IdIntPkMixin

if TYPE_CHECKING:
    from src.task.models import Task


class Activity(TaskTrackerBaseModel, IdIntPkMixin):
    mensuration: Mapped[float] = mapped_column("mensuration")
    done_date: Mapped[datetime] = mapped_column(
        "done_date",
        default=datetime.utcnow(),
        server_default=f"{datetime.utcnow()}",
    )
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    task: Mapped["Task"] = relationship("Task", back_populates="activities")

    __table_args__ = (CheckConstraint("mensuration > 0", name="mensuration_gt_zero"),)
