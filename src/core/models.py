from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class TaskTrackerBaseModel(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"
