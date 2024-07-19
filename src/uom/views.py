from typing import Annotated, TYPE_CHECKING, List
from fastapi import APIRouter, Depends
from src.core.database_helper import database_helper
from src.uom import crud
from src.uom.schemas import UOMRead, UOMCreate

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/uom",
    tags=["Unit of measurement"],
)


@router.get("/", response_model=List[UOMRead])
async def get_uom_list(
    session: Annotated[
        "AsyncSession",
        Depends(database_helper.session_getter),
    ],
):
    return await crud.uom_list(session)


@router.post("/", response_model=UOMRead)
async def add_uom(
    uom: UOMCreate,
    session: Annotated[
        "AsyncSession",
        Depends(database_helper.session_getter),
    ],
):
    return await crud.add_uom(uom, session)
