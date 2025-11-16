from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")



#Find the "search" input by name
driver.maximize_window()
fName= driver.find_element(By.NAME, 'fName')
lName = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
#Sending keyboard input
fName.send_keys('Ahmed')
lName.send_keys('Shweta')
email.send_keys('ahmedsaidmeod@gmail.com')

email.send_keys(Keys.ENTER) 
#alternatively:    driver.find_element(By.CSS_SELECTOR, 'form button').click()


