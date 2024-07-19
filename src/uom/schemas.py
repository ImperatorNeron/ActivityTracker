from typing import Optional

from pydantic import BaseModel, Field


class UOMBase(BaseModel):
    short_title: str = Field(max_length=10)
    full_title: str = Field(max_length=100)


class UOMCreate(UOMBase):
    pass


class UOMPartialUpdate(UOMBase):
    short_title: Optional[str] = Field(max_length=10, default=None)
    full_title: Optional[str] = Field(max_length=100, default=None)


class UOMRead(UOMBase):
    id: int = Field(ge=0)
