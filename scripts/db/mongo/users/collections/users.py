from mongo_util import CollectionBaseClass, mongo_client

from scripts.db.mongo.users.schemas import UserDBSchema


class Users(CollectionBaseClass):
    def __init__(self):
        super().__init__(mongo_client=mongo_client, database="users_db", collection="users")

    def create_user(self, user_data: UserDBSchema):
        return self.insert_one(user_data.model_dump())

    def get_user_by_email(self, email: str):
        return self.find_one({"email": email})

    def get_user_by_id(self, user_id: str):
        return self.find_one({"user_id": user_id})

    def get_all_users(self):
        return self.find(query={})

    def get_user_by_username(self, username: str):
        return self.find_one({"username": username})
