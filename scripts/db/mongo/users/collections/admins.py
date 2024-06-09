from scripts.constants.db_constants import CollectionConstants, DatabaseConstants
from scripts.db.mongo import mongo_client
from scripts.schemas import AdminSchema
from scripts.utils.mongo_util import MongoCollectionBaseClass


class Admins(MongoCollectionBaseClass):
    def __init__(self):
        super().__init__(mongo_client, DatabaseConstants.users_db, CollectionConstants.admins)

    def create_admin(self, admin_data: AdminSchema):
        return self.insert_one(admin_data)

    def get_admin_by_email(self, email: str):
        return self.find_one({"email": email})

    def get_admin_by_id(self, admin_id: str):
        return self.find_one({"user_id": admin_id})

    def get_all_admins(self):
        return self.find(query={})

    def get_root_user(self):
        return self.find_one({"username": "root"})
