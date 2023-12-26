'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a WebDriver instance
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://example.com/login")

# Locate the login fields
username_field = driver.find_element(By.id("username"))
password_field = driver.find_element(By.id("password"))

# Enter the login credentials
username_field.send_keys("username")
password_field.send_keys("password")

# Click the login button
login_button = driver.find_element(By.id("login"))
login_button.click()

# Check the login status
if driver.title.startswith("Account"):
    print("Login successful")
else:
    print("Login failed")

# Close the browser
driver.close()

'''



from bs4 import BeautifulSoup as bs

import pickle

import time
from selenium import webdriver

from configs.get_driver import DRIVERPATH
from configs.argparser import argparser


ASSIGN_URL = 'https://schools.duolingo.com/classroom/6132514/assign'


if __name__ == '__main__':

    user_data_dir = argparser('user_data_dir').user_data_dir


    with open(DRIVERPATH, 'rb') as driverpath:
        chromedriver_bin = pickle.load(driverpath)

    service = webdriver.ChromeService(executable_path=chromedriver_bin)
    options = webdriver.ChromeOptions()

    options.add_argument(f'--user-data-dir={user_data_dir}')

    options.add_argument('--headless') # untouched option
    options.add_argument('--disable-gpu') # when untouched option

    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get(ASSIGN_URL)
        time.sleep(5)
        with open('tmp.html', 'w', encoding="utf-8") as w:
            w.write(driver.page_source)



