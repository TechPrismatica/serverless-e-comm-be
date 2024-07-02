from fastapi import APIRouter
from fastapi.responses import JSONResponse

from scripts.core.handlers.user_handler import UserHandler
from scripts.core.schemas.user import User

user_router = APIRouter()


@user_router.post("/signup")
def create_user(user_data: User):
    try:
        UserHandler().create_user(user_data)
        return JSONResponse(content={"message": "User created successfully"}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=400)
