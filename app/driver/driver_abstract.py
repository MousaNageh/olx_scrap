from abc import ABC, abstractmethod


class DriverAbstract(ABC):
    driver = None

    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def _set_options(self):
        pass
