from abc import ABC, abstractmethod


class ScrapingAbstract(ABC):
    url = "https://www.olx.com.eg/ads/"

    @abstractmethod
    def _send_request(self, url: str):
        pass

    @abstractmethod
    def _handle_url(self, keyword: str):
        pass

    @abstractmethod
    def _handle_data(self, elements):
        pass

    @abstractmethod
    def get_data(self, keyword: str):
        pass
