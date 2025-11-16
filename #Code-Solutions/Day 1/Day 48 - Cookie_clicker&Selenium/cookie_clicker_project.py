from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

def get_upgrade_price(upgrade_name):
    try:
        element = driver.find_element(By.CSS_SELECTOR, f"#{upgrade_name} b")
        text = element.text
        return int(text.split('-')[-1].replace(',', ''))
    except Exception as e:
        print(f"Error getting upgrade price: {e}")
        return 0

def buy_upgrades():
    money = int(driver.find_element(By.ID, 'money').text)
    
    while money>get_upgrade_price('buyCursor'):
        if money >= get_upgrade_price('buyAlchemy\\ lab'):
            driver.find_element(By.ID, 'buyAlchemy lab').click()
        elif money>=get_upgrade_price('buyShipment'):
            driver.find_element(By.ID, 'buyShipment').click()
        elif money>= get_upgrade_price('buyMine'):
            driver.find_element(By.ID, 'buyMine').click()
        elif money>= get_upgrade_price('buyFactory'):
            driver.find_element(By.ID, 'buyFactory').click()
        elif money>= get_upgrade_price('buyGrandma'):
            driver.find_element(By.ID, 'buyGrandma').click()
        else:
            driver.find_element(By.ID, 'buyCursor').click()
        money = int(driver.find_element(By.ID, 'money').text)

last_action_time = time.time()
end_time = last_action_time+30
interval = 5

while True:
    cookie= driver.find_element(By.ID, 'cookie')
    cookie.click()
    current_time = time.time()
    if current_time - last_action_time >= interval:
        buy_upgrades()
        last_action_time = current_time
    if current_time >= end_time:
        print(driver.find_element(By.ID, 'cps').text)
        break


