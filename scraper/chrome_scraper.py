import os

import time
import pickle

from dataclasses import dataclass

from selenium import webdriver

from utils import DRIVERPATH, PAGE_LOAD_SEC, load_chrome_driver



@dataclass
class ChromeScraper:
    user_data_dir: str
    chromedriver_bin_path: str
    driver: webdriver.Chrome


    def __init__(self, user_data_dir: str):
        self.user_data_dir = user_data_dir
        self.chromedriver_bin_path = self.__driver_definer()
        self.driver = webdriver.Chrome(
            service=self.__service(),
            options=self.__options()
        )


    def __enter__(self):
        return self


    def __exit__(self, *args, **kwargs):
        self.quit()


    def wait_webpage_load_totally(self):
        time.sleep(PAGE_LOAD_SEC)


    def quit(self):
        self.driver.quit()


    def __driver_definer(self) -> str:

        if not os.path.exists(DRIVERPATH):
            load_chrome_driver()

        with open(DRIVERPATH, 'rb') as dp:
            chromedriver_bin_path = pickle.load(dp)

        return chromedriver_bin_path


    def __service(self) -> webdriver.ChromeService:
        return webdriver.ChromeService(
            executable_path=self.chromedriver_bin_path
        )


    def __options(self) -> webdriver.ChromeOptions:
        options = webdriver.ChromeOptions()

        # Define User Data directory for using a specific profile
        options.add_argument(f'--user-data-dir={self.user_data_dir}')

        # Untouched option
        options.add_argument('--headless')

        # Disable the Graphics Processing Unit when there is headless mode
        options.add_argument('--disable-gpu')

        return options

