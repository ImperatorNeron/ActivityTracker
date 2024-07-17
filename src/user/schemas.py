from fastapi_users import schemas
from pydantic import BaseModel, Field


class CustomUserBase(BaseModel):
    nickname: str | None = Field(max_length=100)


class UserRead(schemas.BaseUser[int], CustomUserBase):
    pass


class UserCreate(schemas.BaseUserCreate, CustomUserBase):
    pass


class UserUpdate(schemas.BaseUserUpdate, CustomUserBase):
    pass
