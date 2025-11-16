from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

website = "https://www.linkedin.com/jobs/search/?currentJobId=3995663354&f_AL=true&keywords=python%20developer"
email = 'ahmed_saidmedo@yahoo.com'
password = "0102203123123#Aass"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(website)
time.sleep(2)

sign_in = driver.find_element(By.CSS_SELECTOR, '.btn-md.btn-secondary-emphasis')
sign_in.click()
time.sleep(2)

email_entry = driver.find_element(By.ID, 'username')
email_entry.send_keys(email)
password_entry = driver.find_element(By.ID, 'password')
password_entry.send_keys(password)
sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
time.sleep(2)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

driver.get(website)
time.sleep(3)

message_dropdown = driver.find_element(By.XPATH, '/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]')
message_dropdown.click()
print("dropped")
time.sleep(1)

offers_list = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container .job-card-list__title--link')
print(offers_list[0].text)
for item in offers_list:
    print("in loop")
    item.click()
    time.sleep(1)
    save_button = driver.find_elements(By.CSS_SELECTOR, '.mt5 .display-flex')[-1]
    save_button.click()





