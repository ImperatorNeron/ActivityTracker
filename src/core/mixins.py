from typing import TYPE_CHECKING, Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, relationship
from sqlalchemy.orm import mapped_column

if TYPE_CHECKING:
    from src.user.models import User


class IdIntPkMixin:
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )


class UserRelationMixin:
    _nullable: Optional[bool] = False
    _back_populates: Optional[str] = None
    _primary_key: Optional[bool] = False

    @declared_attr
    def user_id(self) -> Mapped[int]:
        return mapped_column(
            ForeignKey("users.id"),
            nullable=self._nullable,
            primary_key=self._primary_key
        )

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=self._back_populates,
        )
