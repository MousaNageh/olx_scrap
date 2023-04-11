from abc import ABC, abstractmethod


class DatabaseConnectionAbstract(ABC):
    @abstractmethod
    def get_db(self):
        pass
