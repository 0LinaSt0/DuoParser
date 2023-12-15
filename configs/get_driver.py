import pickle
from webdriver_manager.chrome import ChromeDriverManager

drivepath = 'materials/chromedriver/chromedriver.pickle'

with open(drivepath, 'wb') as f:
    pickle.dump(ChromeDriverManager().install(), f)

