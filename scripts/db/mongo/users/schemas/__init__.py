from typing import List, Optional

from pydantic import BaseModel


class UserDBSchema(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    username: str
    email: str
    password: str
    is_active: bool = False
    roles: List[str] = ["customer"]
    is_verified: bool = False
    meta: dict
