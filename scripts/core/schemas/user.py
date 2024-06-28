import re
from typing import List, Optional

from pydantic import Field, field_validator

from . import BaseSchema


class User(BaseSchema):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    username: str
    email: str
    password: str = Field(..., min_length=8)


    @field_validator("password")
    def password_complexity(cls, value: str) -> str:
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(pattern, value):
            raise ValueError(
                "Password must have at least 8 characters, one uppercase, one lowercase, one number, and one special character."
            )
        return value
