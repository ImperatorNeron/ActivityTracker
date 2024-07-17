from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable

from src import TaskTrackerBaseModel


class AccessToken(TaskTrackerBaseModel, SQLAlchemyBaseAccessTokenTable[int]):
    pass
