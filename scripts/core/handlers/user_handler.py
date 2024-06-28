import pendulum

from scripts.config import RootUserConfig
from scripts.core.schemas.user import User as UserSchema
from scripts.db.mongo.users.collections.users import Users
from scripts.db.mongo.users.schemas import UserDBSchema
from scripts.exceptions import UserException
from scripts.utils.password_util import encrypt_password


class UserHandler:
    def __init__(self):
        self.users = Users()

    def create_user(self, user_data: UserSchema):
        if self.users.get_user_by_email(user_data.email):
            raise UserException("User already exists with this email")
        elif self.users.get_user_by_username(user_data.username):
            raise UserException("User already exists with this username")
        else:
            user_data.password = encrypt_password(user_data.password)
        user_data = UserDBSchema(**user_data.model_dump())
        return self.users.create_user(user_data)

    def create_admin(self, admin_data):
        return self.admins.create_admin(admin_data)

    def get_user_by_email(self, email):
        return self.users.get_user_by_email(email)

    def get_user_by_id(self, user_id):
        return self.users.get_user_by_id(user_id)

    def get_all_users(self):
        return self.users.get_all_users()

    def get_root_user(self):
        return self.users.get_user_by_username(RootUserConfig.ROOT_USERNAME)

    def create_root_user(self):
        user = UserDBSchema(
            username=RootUserConfig.ROOT_USERNAME,
            email=RootUserConfig.ROOT_USER_EMAIL,
            first_name=RootUserConfig.ROOT_FIRST_NAME,
            last_name=RootUserConfig.ROOT_LAST_NAME,
            password=encrypt_password(RootUserConfig.ROOT_USER_PASSWORD),
            is_verified=True,
            meta={
                "created_at": pendulum.now(tz="UTC").int_timestamp,
                "updated_at": pendulum.now(tz="UTC").int_timestamp,
            },
            roles=["admin"],
            is_active=True,
        )
        Users().create_user(user)
