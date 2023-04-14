from abc import ABC, abstractmethod

from pymongo import MongoClient
from datetime import date

class DatabaseConnectionAbstract(ABC):

    @abstractmethod
    def __init__(self,db:MongoClient):
        pass


    @abstractmethod
    def get_if_exists(self,keyword:str):
        pass

    @abstractmethod
    def create_doc(self, keyword: str,data):
        pass