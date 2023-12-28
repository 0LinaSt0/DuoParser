import pickle

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from utils.get_driver import DRIVERPATH
from utils.argparser import argparser

from sortedcontainers import SortedSet

from tqdm.auto import tqdm

import json


from utils.argparser import get_arguments
from scraper.words_scraper import WordsScraper


def lets_scrape():
    user_data_dir, class_id, attachment_name, main_union_number, level_name = get_arguments()

    with WordsScraper(user_data_dir, class_id) as scraper:
        scraper.get_words()

        scraper.save_words_by_unit_to_json(main_union_number, attachment_name)

        scraper.save_words_by_level_to_json(level_name, attachment_name)



if __name__ == '__main__':

    CLASSROOM_URL = 'https://schools.duolingo.com/classroom/'

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
        (('-n', '--filename'), conf1)
    )

    user_data_dir, class_id = args.user_data_dir, args.class_id
    filename = args.filename if args.filename else f'class_{class_id}_words.json'

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

            words = SortedSet()

            if n_words:
                points = unit.find_elements(
                    By.CSS_SELECTOR,
                    'div._2i_uN'
                )

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

            u_words[n_unit] = (level, len(words), list(words))

            progress_bar.update(1)

        with open(f'data/{filename}', 'w', encoding='utf-8') as f:
            json.dump(u_words, f, ensure_ascii=False)


