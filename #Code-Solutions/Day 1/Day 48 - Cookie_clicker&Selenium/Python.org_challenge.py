from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), )
driver.get("https://www.python.org")

event_names = driver.find_elements(By.CSS_SELECTOR, '.medium-widget.event-widget.last ul.menu li a') 
events_dates = driver.find_elements(By.CSS_SELECTOR, '.medium-widget.event-widget.last time') 

results = dict_of_dicts = {i: {"name": name.text, "date": date.text} for i, (name, date) in enumerate(zip(event_names, events_dates))}
print(results)

input("press enter to exit")
driver.quit()