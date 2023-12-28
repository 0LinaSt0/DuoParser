from .conf import (
    PAGE_LOAD_SEC,
    DRIVERPATH,
    WORDS_DIR,
    WEBPAGES_DIR,
    CLASSROOM_URL,
    ELEMENT
)
from .argparser import get_arguments
from .get_driver import load_chrome_driver
from .words_split import split_to_words
