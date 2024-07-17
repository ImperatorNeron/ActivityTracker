from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from fastapi.responses import ORJSONResponse

from src.core.database_helper import database_helper
from src.core.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await database_helper.dispose()


application = FastAPI(
    title="Task Tracker", default_response_class=ORJSONResponse, lifespan=lifespan
)
application.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:application", reload=True)
