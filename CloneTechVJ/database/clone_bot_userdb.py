import motor.motor_asyncio
from info import CLONE_DATABASE_URI, DATABASE_NAME

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.user = self.db.user


db = Database(CLONE_DATABASE_URI, DATABASE_NAME)
