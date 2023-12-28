import pickle
from webdriver_manager.chrome import ChromeDriverManager

from .conf import DRIVERPATH


def load_chrome_driver() -> None:
    with open(DRIVERPATH, 'wb') as f:
        pickle.dump(ChromeDriverManager().install(), f)

