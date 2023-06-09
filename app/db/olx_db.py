from pymongo import MongoClient
from db.abstraction.collection_abstract import DatabaseConnectionAbstract
from datetime import date

class OlxCollections(DatabaseConnectionAbstract):

    def __init__(self, db:MongoClient):
        self.db = db
        self.collection_name ="olx_collection"
        self.collection = self.db[self.collection_name]

    def get_if_exists(self,keyword:str):
        today = str(date.today())
        return self.collection.find_one({"keyword":keyword,"date":today})

    def create_doc(self, keyword: str, data):
        today = str(date.today())
        query = self.collection.insert_one({"keyword":keyword,"date":today,"data":data})
        return  self.collection.find_one({"_id": query.inserted_id})




