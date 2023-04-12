from pymongo import MongoClient
from db.abstraction.db_connection_abstract import DatabaseConnectionAbstract
import os


class DatabaseConnection(DatabaseConnectionAbstract):
    def get_db(self) :
        client = MongoClient(host=os.environ.get('DATABASE_HOST'),
                             port=int(os.environ.get('DATABASE_PORT')),
                             username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'),
                             password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'),
                             authSource=os.environ.get('DATABASE_AUTH_SOURCE'))
        db = client[os.environ.get("MONGO_INITDB_DATABASE")]
        return db
