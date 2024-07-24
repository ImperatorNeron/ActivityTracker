from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(max_length=100)
    description: Optional[str] = None
    start_value: float = Field(ge=0, default=0)
    goal_value: float = Field(ge=0)
    start_date: Optional[datetime] = None
    finish_date: Optional[datetime] = None
    folder_id: Optional[int] = Field(ge=0, default=None)


class ReadTask(TaskBase):
    id: int = Field(ge=0)
    creation_date: datetime


class CreateTask(TaskBase):
    pass


class UpdateTask(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    start_value: Optional[float] = None
    goal_value: Optional[float] = None
    start_date: Optional[datetime] = None
    finish_date: Optional[datetime] = None
    folder_id: Optional[int] = None
