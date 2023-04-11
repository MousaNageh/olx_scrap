from driver.driver_abstract import DriverAbstract
from selenium import webdriver
import os


class ChromeDriver(DriverAbstract):

    def get_driver(self):
        return webdriver.Chrome(options=self._set_options(), executable_path=os.environ.get("CHROMEDRIVER_PATH"))

    def _set_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.headless = True
        return options
