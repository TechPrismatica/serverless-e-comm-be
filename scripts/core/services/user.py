from fastapi import APIRouter
from fastapi.responses import JSONResponse

from scripts.core.handlers.user_handler import UserHandler
from scripts.core.schemas.user import User as UserSchema

user_router = APIRouter()


@user_router.post("/create_user")
def create_user(user_data: UserSchema):
    if UserHandler().create_user(user_data):
        return JSONResponse(content={"message": "User created successfully"}, status_code=201)
