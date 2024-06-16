import pendulum

from scripts.db.mongo.users.collections.admins import Admins
from scripts.db.mongo.users.collections.users import Users
from scripts.schemas import AdminSchema, UserSchema


class UserHandler:
    def __init__(self):
        self.users = Users()
        self.admins = Admins()

    def create_user(self, user_data):
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
        return self.admins.get_root_user()

    def create_root_user(self):
        user = UserSchema(
            email="serverless.e-comm.root@gmail.com",
            first_name="root",
            last_name="root",
            password="root",
            is_admin=True,
            is_verified=True,
            created_at=pendulum.now(tz="UTC").int_timestamp,
            updated_at=pendulum.now(tz="UTC").int_timestamp,
        )
        Users().create_user(user.model_dump())
        Admins().create_admin(AdminSchema(**user.model_dump()).model_dump())
