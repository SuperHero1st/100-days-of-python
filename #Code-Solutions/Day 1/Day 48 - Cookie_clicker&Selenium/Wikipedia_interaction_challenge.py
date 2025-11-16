from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# articles_count.click()

#Find element by link text
portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# portals.click()

#Find the "search" input by name
driver.maximize_window()
search= driver.find_element(By.NAME, 'search')
#Sending keyboard input
search.send_keys('python')
search.send_keys(Keys.ENTER)
