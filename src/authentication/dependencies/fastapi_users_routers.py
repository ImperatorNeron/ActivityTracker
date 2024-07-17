from fastapi_users import FastAPIUsers

from src.user.models import User
from src.authentication.dependencies.user_manager import get_user_manager
from src.authentication.dependencies.backend import authentication_backend

fastapi_users_routers = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)
