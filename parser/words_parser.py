import json

from tqdm.auto import tqdm

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from typing import Tuple, Dict, List
from sortedcontainers import SortedSet

from utils import split_to_words
from utils import CLASSROOM_URL, WEBPAGES_DIR, WORDS_DIR, ELEMENT
from .chrome_parser import ChromeParser


class WordsParser(ChromeParser):
    class_id: str
    assign_url: str
    page_source: str
    words: Dict[int, Tuple[str, int, List[str]]] = dict()


    def __init__(self, user_data_dir: str, class_id: str):
        super().__init__(user_data_dir)
        self.class_id = class_id

        self.assign_url = CLASSROOM_URL + class_id + '/assign'

        self.driver.get(self.assign_url)
        self.wait_webpage_load_totally()

        self.page_source = self.driver.page_source


    def save_webpage(self, attach: str = '') -> None:
        as_html = '_webpage.html'

        filename = (attach + as_html) if len(attach) else (self.class_id + as_html)

        filepath = WEBPAGES_DIR + filename

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self.page_source)
        except Exception as e:
            # ADD LOGGER STATEMENT
            ...


    def save_words_by_unit_to_json(
        self, n_unit: int = 0, attach: str = ''
    ) -> None:

        if n_unit:
            by_unit = f'_words_by_unit_{n_unit}.json'
            words = SortedSet()

            for key, value in self.words.items():
                if int(key) > n_unit:
                    break
                words.update(value[2])

            words = list(words)
        else:
            by_unit = '_words_by_units.json'
            words = self.words

        filename = (attach + by_unit) if len(attach) else (self.class_id + by_unit)

        filepath = WORDS_DIR + filename

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(words, f, ensure_ascii=False)
        except Exception as e:
            # ADD LOGGER STATEMENT
            ...


    def save_words_by_level_to_json(
        self, level_name, attach: str = ''
    ) -> None:

        if len(level_name) == 0:
            return

        by_level = f'_words_by_level_{level_name}.json'

        words = SortedSet()

        for unit in self.words.values():
            if unit[0] == level_name:
                words.update(unit[2])

        words = list(words)

        filename = (attach + by_level) if len(attach) else (self.class_id + by_level)

        filepath = WORDS_DIR + filename

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(words, f, ensure_ascii=False)
        except Exception as e:
            # ADD LOGGER STATEMENT
            ...


    def get_words(self) -> None:
        units = self.driver.find_elements(By.CSS_SELECTOR, ELEMENT['UNITS'])

        progress_bar = tqdm(range(len(units)))

        for unit in units:
            n_unit, level, n_words = self.__header_pars(unit)

            u_words = []

            if n_words:
                u_words = self.__words_pars(unit)

            self.words[n_unit] = (level, len(u_words), u_words)

            progress_bar.update(1)


    def __header_pars(self, unit) -> Tuple[int, str, int]:
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
                ELEMENT['U_HEADER']
            ).text.split('\n')

        # BETTER WAY TO USE XPATH INSTEAD OF [id]
        # u = unit_header.find_element(By.XPATH, "//*[contains(text(), 'Unit')]").split()

        n_unit = int(unit_header[0].split()[1])
        level = unit_header[2]
        n_words = int(unit_header[3].split()[0])

        return n_unit, level, n_words


    def __words_pars(self, unit) -> List[str]:
        words = SortedSet()

        points = unit.find_elements(By.CSS_SELECTOR, ELEMENT['U_POINTS'])

        for point in points:
            try:
                point.find_element(
                    By.CSS_SELECTOR, ELEMENT['BUTTON_SHOW_WORDS']
                ).click()
            except NoSuchElementException:
                pass

            l_point_words = point.find_elements(
                By.CSS_SELECTOR, ELEMENT['WORDS']
            )

            for point_words in l_point_words:
                words.update(split_to_words(point_words.text))

        return list(words)


