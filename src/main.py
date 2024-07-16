from fastapi import FastAPI
import uvicorn

from src.core.router import router

application = FastAPI(title="Task Tracker")
application.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:application", reload=True)
