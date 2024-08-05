from typing import TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from src import Activity, Task
from src.activity.schemas import ActivityCreate
from src.core.crud import get_user_item_by_id

if TYPE_CHECKING:
    from sqlalchemy import Result


async def get_user_task_activity(
    task_id: int,
    user_id: int,
    session: AsyncSession,
):
    task = await get_user_item_by_id(Task, task_id, user_id, session)
    result: "Result" = await session.execute(
        select(Activity).filter(
            and_(
                Activity.task_id == task_id,
                task.user_id == user_id,
            ),
        )
    )
    return list(result.scalars().all())


async def add_activity(
    activity_in: ActivityCreate,
    user_id: int,
    session: AsyncSession,
):
    if activity_in.task_id is not None:
        await get_user_item_by_id(Task, activity_in.task_id, user_id, session)

    activity_new = Activity(**activity_in.model_dump())
    session.add(activity_new)
    await session.commit()
    return activity_new
