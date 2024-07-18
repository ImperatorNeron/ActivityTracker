from sqlalchemy import MetaData, Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from src.core.settings import settings


class TaskTrackerBaseModel(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.database.naming_convention)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)

    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"
