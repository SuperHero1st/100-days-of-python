from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

website = "https://x.com"
PROMISED_UP = 4.5
PROMISED_DOWN= 30
EMAIL = 'ahmedsaidmeod2@gmail.com'
PASSWORD = "0102203123123#Aass"


# class InternetSpeedTwitterBot:
#     def __init__(self) -> None:
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#         self.down = 0
#         self.up = 0

#     def get_internet_speed(self):
#         pass


#     def tweet_at_provider(self):
#         pass

# bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# bot.tweet_at_provider()

test_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
test_driver.get('https://www.speedtest.net/')
go_button = test_driver.find_elements(By.CLASS_NAME, 'start-button')
for element in go_button:
    print(element)
# time.sleep(5)
# go_button.click()


