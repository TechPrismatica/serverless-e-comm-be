from mongo_util import CollectionBaseClass, mongo_client

from scripts.core.schemas.user import User


class Users(CollectionBaseClass):
    def __init__(self):
        super().__init__(mongo_client=mongo_client, database="metadata", collection="users")

    def create_user(self, user_data: User):
        return self.insert_one(user_data)

    def get_user_by_email(self, email: str):
        return self.find_one({"email": email})

    def get_user_by_id(self, user_id: str):
        return self.find_one({"user_id": user_id})

    def get_all_users(self):
        return self.find(query={})
