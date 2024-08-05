from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ActivityBase(BaseModel):
    mensuration: float = Field(ge=0)
    task_id: int = Field(ge=0)


class ActivityRead(ActivityBase):
    id: int = Field(ge=0)
    done_date: datetime = Field(examples=["2024-08-04T15:02:36.351052"])


class ActivityCreate(ActivityBase):
    pass


class ActivityPatch(ActivityBase):
    mensuration: Optional[float] = None
    task_id: Optional[int] = None
