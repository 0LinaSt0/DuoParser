import pickle
from webdriver_manager.chrome import ChromeDriverManager


__all__ =['DRIVERPATH']


DRIVERPATH = 'materials/chromedriver/chromedriver.pickle'

with open(DRIVERPATH, 'wb') as f:
    pickle.dump(ChromeDriverManager().install(), f)

