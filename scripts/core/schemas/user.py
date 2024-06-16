from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    username: str
    email: str
    password: str
    is_active: bool = False
    roles: list[str]
    is_verified: bool = False
    meta: dict
