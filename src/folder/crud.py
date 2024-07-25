from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, and_
from fastapi import status

from src import Task, Folder
from src.core.crud import delete_item_by_user_id, get_user_item_by_id


async def delete_tasks_and_folder(
    folder_id: int,
    user_id: int,
    session: AsyncSession,
):
    folder = await get_user_item_by_id(Folder, folder_id, user_id, session)
    if folder:
        await session.execute(
            delete(Task).where(
                and_(Task.user_id == user_id, Task.folder_id == folder_id),
            )
        )
        await session.commit()
        await delete_item_by_user_id(Folder, folder_id, user_id, session)

    return {"status_code": status.HTTP_204_NO_CONTENT}
