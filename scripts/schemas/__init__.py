from pydantic import BaseModel


class UserSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool = True
    is_admin: bool = False
    is_verified: bool = False
    created_at: str
    updated_at: str


class AdminSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool = True
    is_admin: bool = True
    is_verified: bool = False
    created_at: str
    updated_at: str
