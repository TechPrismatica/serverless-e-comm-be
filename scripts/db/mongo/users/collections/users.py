from scripts.constants.db_constants import CollectionConstants, DatabaseConstants
from scripts.db.mongo import mongo_client
from scripts.schemas import UserSchema
from scripts.utils.mongo_util import MongoCollectionBaseClass


class Users(MongoCollectionBaseClass):
    def __init__(self):
        super().__init__(mongo_client, DatabaseConstants.users_db, CollectionConstants.users)

    def create_user(self, user_data: UserSchema):
        return self.insert_one(user_data)

    def get_user_by_email(self, email: str):
        return self.find_one({"email": email})

    def get_user_by_id(self, user_id: str):
        return self.find_one({"user_id": user_id})

    def get_all_users(self):
        return self.find(query={})
