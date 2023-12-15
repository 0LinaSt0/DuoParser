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

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.opera import OperaDriverManager

from conf import HEADERS, HEADERS_GET


PAYLOAD = {
    'login': 'lina.stof@mail.ru',
    'password': 'Readytakemywords23'
}


# LOGIN_URL = 'https://santa-secret.ru/login'
LOGIN_URL = 'https://schools.duolingo.com/login'
# LOGIN_URL = 'https://www.duolingo.com/2017-06-30/login?fields='
# ASSIGN_URL = 'https://schools.duolingo.com/api/2/observers/classroom_assignments?classroom_id=6132514&_=1702472856447'
ASSIGN_URL = 'https://schools.duolingo.com/classroom/6132514/assign'
# ASSIGN_URL = 'https://www.google-analytics.com/collect?v=1&_v=j101&a=1241458826&t=pageview&_s=1&dl=https%3A%2F%2Fschools.duolingo.com%2Fclassroom%2F6132514%2Fassign&dr=https%3A%2F%2Fyandex.ru%2F&ul=ru&de=UTF-8&dt=Duolingo%20for%20Schools&sd=24-bit&sr=1920x1200&vp=512x1043&je=0&cn=&cs=&cm=&ck=&cc=&_u=SACAAEABAAAAACgAIAC~&jid=&gjid=&cid=1300570805.1702452917&tid=UA-21595814-23&_gid=1756163213.1702452917&gtm=45He3bt0n81NXRLZVSv843402430&gcd=11l1l1l1l1&dma=0&z=3746740'


# edge_bin = r'C:\Users\hristoforova\Desktop\Prgrmn\DuoScraper\materials\IEdriver\IEDriverServer.exe'
edge_bin = './materials/IEdriver/IEDriverServer.exe'
chromedriver_bin = './materials/chromedriver/chromedriver.exe'

service = webdriver.ChromeService(executable_path=chromedriver_bin)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# with webdriver.Chrome(service=service, options=options) as driver:
driver = webdriver.Chrome(service=service, options=options)
driver.get(LOGIN_URL)
time.sleep(1)
'''
login:
//*[@id="root"]/div[1]/div/div[2]/form/div[1]/div[1]/div[1]/label/div/input

password:
//*[@id="root"]/div[1]/div/div[2]/form/div[1]/div[1]/div[2]/label/div[1]/input
'''
username_xpath = r'//*[@id="root"]/div[1]/div/div[2]/form/div[1]/div[1]/div[1]/label/div/input'
password_xpath = r'//*[@id="root"]/div[1]/div/div[2]/form/div[1]/div[1]/div[2]/label/div[1]/input'
login_button_xpath = r'//*[@id="root"]/div[1]/div/div[2]/form/div[1]/button'

username_field = driver.find_element(By.XPATH, username_xpath)
password_field = driver.find_element(By.XPATH, password_xpath)
login_button = driver.find_element(By.XPATH, login_button_xpath)

username_field.send_keys(PAYLOAD['login'])
password_field.send_keys(PAYLOAD['password'])
login_button.click()

time.sleep(1)

if driver.title.startswith("Account"):
    print("Login successful")
else:
    print("Login failed")

    # print(driver.page_source)


exit()
options = webdriver.IeOptions()
# options.ignore_protected_mode_settings = True
# options.native_events = True
# options.ignore_zoom_level = True
# options.require_window_focus = True

# cap = DesiredCapabilities().INTERNETEXPLORER
# cap['ignoreProtectedModeSettings'] = True
# cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
# cap['nativeEvents'] = True
# cap['ignoreZoomSetting'] = True
# cap['requireWindowFocus'] = True
# cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True

service = webdriver.IeService(executable_path=edge_bin)
with webdriver.Ie(service=service, options=options) as driver:
    driver.get(LOGIN_URL)
    time.sleep(2)
    print(driver.page_source)

exit()



'''
By requests
'''
# with requests.Session() as s:
    # res = s.post(LOGIN_URL, headers=HEADERS, json=PAYLOAD)
    # res.encoding = 'ISO-8859-1'
    # print(dir(res.request))
    # print(res.request.body)
    # print(res.request.url)
    # print(res.request.hooks)
    # print(res.text)
    # print(res.status_code)
    # soup = bs(res.text, features='html.parser')
    # nonce = soup.find('input')
    # print(res.content)
    # print(soup)

    # r = s.get(ASSIGN_URL, headers=HEADERS_GET)
    # print(dir(r))
    # print(r.request)
    # print(r.status_code)
    # print(r.text)
    # r = s.get('https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP#406')
    # print(r.status_code)
