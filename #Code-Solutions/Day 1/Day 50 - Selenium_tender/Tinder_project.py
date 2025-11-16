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

website = "https://tinder.com"
email = 'ahmed_saidmedo@yahoo.com'
password = "0102203123123#Aass"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(website)
time.sleep(2)

#Mx(12px).Mx(8px)--m 

sign_in_button = driver.find_element(By.XPATH, '//*[@id="u849573418"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
sign_in_button.click()
time.sleep(1)

lop_in_with_facebook = driver.find_element(By.XPATH, '//*[@id="u-878807658"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
lop_in_with_facebook.click()
time.sleep(2)

#Changing focused window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_entry = driver.find_element(By.CSS_SELECTOR, 'input#email')
email_entry.send_keys(email)

email_entry = driver.find_element(By.CSS_SELECTOR, 'input#pass')
email_entry.send_keys(password)

log_in_button = driver.find_element(By.XPATH, "//input[@name='login' and @value='Log in']")
log_in_button.click()
time.sleep(10)

# Wait for the continue button to be present and clickable
try:
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@id,"mount_0_0")]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span'))
    )
    continue_button.click()
except Exception as e:
    print(f"An error occurred: {e}")()

driver.switch_to.window(base_window)
print(driver.title)

# input("Press Enter when you have solved the Captcha")

# driver.get(website)
# time.sleep(3)

# message_dropdown = driver.find_element(By.XPATH, '/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]')
# message_dropdown.click()
# print("dropped")
# time.sleep(1)

# offers_list = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container .job-card-list__title--link')
# print(offers_list[0].text)
# for item in offers_list:
#     print("in loop")
#     item.click()
#     time.sleep(1)
#     save_button = driver.find_elements(By.CSS_SELECTOR, '.mt5 .display-flex')[-1]
#     save_button.click()





