# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# chromedriver_bin = './materials/chromedriver/chromedriver.exe'
# LOGIN_URL = 'accounts.google.com/signin'

# service = webdriver.ChromeService(executable_path=chromedriver_bin)
# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')

# # with webdriver.Chrome(service=service, options=options) as driver:
# driver = webdriver.Chrome(service=service, options=options)
# driver.get(LOGIN_URL)
# time.sleep(1)


# email_input = driver.find_element_by_id('identifier')
# email_input.send_keys('p.hristoforova')

# password_input = driver.find_element_by_id('password')
# password_input.send_keys('24Fotobe')

# login_button = driver.find_element_by_id('signIn')
# login_button.click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle

import configs

# Replace 'path_to_chromedriver' with the path to your ChromeDriver executable
# chromedriver_bin = './materials/chromedriver/chromedriver.exe'
# chromedriver_bin = r'C:\Users\hristoforova\Desktop\Prgrmn\DuoScraper\materials\chromedriver\chromedriver.exe'
with open(configs.get_driver.drivepath, 'rb') as f:
    chromedriver_bin = pickle.load(f)

# LOGIN_URL = 'accounts.google.com/signin'
LOGIN_URL = 'https://accounts.google.com/signin'
LOGIN_URL = 'https://gmail.com'


from seleniumbase       import Driver
from time                          import sleep
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as EC

class Google:
    def __init__(self) -> None:

        self.url    = LOGIN_URL#'https://accounts.google.com/ServiceLogin'
        self.driver = Driver(
            uc=True, incognito=True, driver=
            # options=webdriver.ChromeOptions(),
            # service=webdriver.ChromeService(chromedriver_bin)
        )
        try:
            self.driver.get(self.url)
            self.time   = 10
        except Exception as e:
            print(e)
            print("DONE")
            self.driver.quit()

    # def login(self, email, password):
    #     print('is_here')
    #     sleep(2)
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
    #     sleep(2)
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')

    #     self.code()

    # def code(self):
    # # [ ---------- paste your code here ---------- ]
    #     sleep(self.time)

if __name__ == "__main__":
    #  ---------- EDIT ----------
    email = 'p.hristoforova' # replace email
    password = '24Fotobe' # replace password
    #  ---------- EDIT ----------

    google = Google()
        # google.login(email, password)



exit()

service = webdriver.ChromeService(executable_path=chromedriver_bin)
options = webdriver.ChromeOptions()
# options.accept_untrusted_certs = True
# options.assume_untrusted_cert_issuer = True
# options.add_argument("--no-sandbox")
# options.add_argument("--allow-http-screen-capture")
# options.add_argument("--disable-impl-side-painting")
# options.add_argument("--disable-setuid-sandbox")
# options.add_argument("--disable-seccomp-filter-sandbox")
# options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 Safari/537.36')
# options.add_argument('--headless')
try:
    driver = webdriver.Chrome(service=service, options=options)

    # Use the new_window command to open a new window
    # driver.execute_cdp_cmd('Browser.createWindow')

    # Switch to the new window
    # driver.switch_to.window(driver.window_handles[1])


    # Open the Google login page
    driver.get(LOGIN_URL)

    # Find and fill in the email field
    email_field = driver.find_element(By.ID, 'identifierId')
    email_field.send_keys('p.hristoforova')

    # Click the "Next" button
    email_field.send_keys(Keys.RETURN)

    # Wait for the password field to load
    time.sleep(2)

    # Find and fill in the password field
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('24Fotobe')

    # Click the "Next" button
    password_field.send_keys(Keys.RETURN)

    # Wait for the login to complete
    time.sleep(10)
except:
    input()
# Close the browser
driver.quit()
print(r'I\'m done')

