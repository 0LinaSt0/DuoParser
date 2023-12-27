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

import pickle

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from configs.get_driver import DRIVERPATH
from configs.argparser import argparser

from sortedcontainers import SortedSet

from tqdm.auto import tqdm

import json


CLASSROOM_URL = 'https://schools.duolingo.com/classroom/'


if __name__ == '__main__':

    conf = {
        'type':str,
        'help': 'Path to User Data directory',
        'required':True
    }

    conf1 = {
        'nargs':'?',
        'const': None,
        'type': str,
        'help': 'Name of output json with words'
    }

    args = argparser(
        (('-d', '--user_data_dir'), conf),
        (('-i', '--class_id'), conf),
        (('-n', '--json_name'), conf1)
    )

    user_data_dir, class_id = args.user_data_dir, args.class_id
    json_name = args.json_name if args.json_name else f'class_{class_id}_words.json'

    assign_url = CLASSROOM_URL + class_id + '/assign'

    with open(DRIVERPATH, 'rb') as driverpath:
        chromedriver_bin = pickle.load(driverpath)

    service = webdriver.ChromeService(executable_path=chromedriver_bin)
    options = webdriver.ChromeOptions()

    options.add_argument(f'--user-data-dir={user_data_dir}')

    options.add_argument('--headless') # untouched option
    options.add_argument('--disable-gpu') # when untouched option

    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get(assign_url)
        time.sleep(5)
        # with open('tmp.html', 'w', encoding="utf-8") as w:
        #     w.write(driver.page_source)

        units = driver.find_elements(By.CSS_SELECTOR, 'section.KF0CX')

        u_words = {}

        progress_bar = tqdm(range(len(units)))

        for unit in units:
            '''
            Structure of Unit's header text in unit_header list:
            [
                'Unit {#}',
                '{unit_description}',
                '{unit_level}',
                '{#} words',
                'Current Students: {#}'
            ]
            '''
            unit_header = unit.find_element(
                    By.CSS_SELECTOR,
                    'header._3LSiE > div._2Z-Z4'
                ).text.split('\n')

            n_unit = int(unit_header[0].split()[1])
            level = unit_header[2]
            n_words = int(unit_header[3].split()[0])


            if n_words:
                points = unit.find_elements(
                    By.CSS_SELECTOR,
                    'div._2i_uN'
                )

                words = SortedSet()
                for point in points:
                    try:
                        point.find_element(
                            By.CSS_SELECTOR, 'div > button.kRgiM'
                        ).click()
                    except NoSuchElementException:
                        pass

                    l_point_words = point.find_elements(
                        By.CSS_SELECTOR,
                        'div > div._3ewMG > div._1dAI3 > div._3D4G0 > p._2HH61'
                    )

                    for point_words in l_point_words:
                        words.update(point_words.text.split(', '))

            u_words[n_unit] = (level, n_words, words)

            progress_bar.update(1)

        with open(f'data/class_{class_id}_words.json', 'w', encoding='utf-8') as f:
            json.dump(list(u_words), f)


