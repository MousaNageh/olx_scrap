from selenium.webdriver.support.wait import WebDriverWait

from scraping.abstraction.scraping_abstract import ScrapingAbstract
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
class OlxScraping(ScrapingAbstract):


    def __init__(self,driver):
        self.driver = driver
    def _handle_url(self, keyword: str):
        return self.url + f"q-{keyword}/"

    def _send_request(self, url: str):
        self.driver.get(url)

    def _handle_data(self, elements):
        results = []
        for element in elements:
            item = self.__get_one_item()
            item["title"] = self.__scraping_title(element)
            item["image"] = self.__scraping_img_url(element)
            item["price"], item["currency"], item["negotiable"] = self.__scraping_price(element)
            item["location"] = self.__scraping_location(element)
            item["created_at"] = self.__scraping_created_at(element)

            results.append(item)
        return results

    def get_data(self, keyword: str):
        page = 1
        data=[]
        url = self._handle_url(keyword)
        while len(data) < 10:
            url_paginate = url if page == 1 else f"{url}?page={page}"
            self._send_request(url_paginate)
            try:
                self.driver.find_elements(By.XPATH, "//li[@aria-label='Listing']")
            except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
                break
            lis = self.driver.find_elements(By.XPATH, "//li[@aria-label='Listing']")
            if not len(lis):
                break
            data += self._handle_data(lis)
            page += 1
        self.driver.quit()
        return data

    def __scraping_img_url(self, li):
        try:

            img_div = li.find_element(By.XPATH, "//div[@class='ee2b0479']")
            source = img_div.find_element(By.TAG_NAME, "source")
            return source.get_attribute('srcset')
        except Exception as e:
            print(e)

    def __scraping_title(self, li):
        try:

            title = li.find_element(By.XPATH, "//div[@aria-label='Title']")
            return title.text.strip()
        except Exception as e:
            print(e)

    def __scraping_price(self, li):
        price_obj = {
            "price": None,
            "currency": None,
            "negotiable": None
        }
        try:

            price_div = li.find_element(By.XPATH, "//div[@aria-label='Price']")
            price_spans = price_div.find_elements(By.TAG_NAME, "span")
            price_obj["price"], price_obj["currency"] = price_spans[0].text.strip().split(" ")[:2]
            price_obj["price"] = int(price_obj["price"].replace(",", ""))
            if len(price_spans) >1:
                price_obj["negotiable"] = price_spans[1].text.strip()

            return price_obj

        except Exception as e:
            print(e)
            return price_obj

    def __scraping_location(self, li):
        try:
            location = li.find_element(By.XPATH, "//span[@aria-label='Location']")
            return location.text.strip().replace("•", "")
        except Exception as e:
            print(e)

    def __scraping_created_at(self, li):
        try:
            created_at = li.find_element(By.XPATH, "//span[@aria-label='Creation date']")
            return created_at.text.strip()
        except Exception as e:
            print(e)

    def __get_one_item(self):
        return {
            "image": None,
            "title": None,
            "price": None,
            "currency": None,
            "negotiable": None,
            "location": None,
            "created_at": None
        }