from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FolderBase(BaseModel):
    title: str = Field(max_length=100)
    description: Optional[str]
    tasks_quantity: int = Field(ge=0, default=0)


class FolderRead(FolderBase):
    creation_date: datetime


class FolderCreate(FolderBase):
    pass


class FolderUpdate(FolderBase):
    pass
