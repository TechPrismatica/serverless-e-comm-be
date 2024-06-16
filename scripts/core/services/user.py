from fastapi import APIRouter
from tp_auth_jwt import AuthInfo

user_router = APIRouter()


@user_router.get("/users/me")
async def get_user(auth_info: AuthInfo):
    return auth_info.user
