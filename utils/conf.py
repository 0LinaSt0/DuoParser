
__all__ = [
    'DRIVERPATH',
    'CLASSROOM_URL',
    'ELEMENT',
    'PAGE_LOAD_SEC',
    'WORDS_DIR',
    'WEBPAGES_DIR'
]


ELEMENT = {
    'UNITS': 'section.KF0CX',
    'U_HEADER': 'header._3LSiE > div._2Z-Z4',
    'U_POINTS': 'div._2i_uN',
    'BUTTON_SHOW_WORDS': 'div > button.kRgiM',
    'WORDS': 'div > div._3ewMG > div._1dAI3 > div._3D4G0 > p._2HH61'
}


DRIVERPATH = 'materials/chromedriver/chromedriver.pickle'

DATA_DIR = 'data/'
WORDS_DIR = DATA_DIR + 'words/'
WEBPAGES_DIR = DATA_DIR + 'webpages/'

CLASSROOM_URL = 'https://schools.duolingo.com/classroom/'

PAGE_LOAD_SEC = 5

