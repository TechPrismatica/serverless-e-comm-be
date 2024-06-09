from scripts.config import Databases
from scripts.utils.mongo_util import MongoConnect

mongo_client = MongoConnect(uri=Databases.MONGO_URI)()
