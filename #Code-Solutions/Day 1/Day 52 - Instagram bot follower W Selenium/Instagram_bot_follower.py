from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time

website = "https://www.instagram.com/accounts/login/"
# email = 'datadirectcareer@gmail.com'
# password = "0102203123123#Aass"
email = 'boxer_ck_home'
password = "01276621256#Noah"

class InstaFollower:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def login(self):
        self.driver.get(website)
        time.sleep(3)
        email_entry = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_entry.send_keys(email)
        time.sleep(1)
        password_entry = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_entry.send_keys(password)
        time.sleep(0.5)
        password_entry.send_keys(Keys.ENTER)
        time.sleep(5)

        #Turn on notification, clicking Not now
        try:
            Not_Now_prompt = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Not Now')]")
            Not_Now_prompt.click()
        except:
            pass

    def find_followers(self):
        time.sleep(1)
        self.driver.get('https://www.instagram.com/outerwear_and_underwear/')
        time.sleep(3)
        followers_button = self.driver.find_element(By.XPATH, value="//a[contains(text(), 'followers')]")
        followers_button.click()
        time.sleep(3.5)

        scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class, '_acan _acap _acas')]")
        for button in follow_buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                button.click()
                time.sleep(1)

            except ElementClickInterceptedException:
                try:
                    cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                except Exception as e:
                    print(e)
                    pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()



