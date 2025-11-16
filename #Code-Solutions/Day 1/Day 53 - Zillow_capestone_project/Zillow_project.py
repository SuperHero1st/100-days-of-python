from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time

zillow_website = 'https://appbrewery.github.io/Zillow-Clone/'
google_forms_url = 'https://docs.google.com/forms/d/e/1FAIpQLScreSCHSyrZP9T0PmaQwN0-MD4mg2hZFOyZ2fdlI5Uguzqj5g/viewform'
links_list = []
prices_list= []
addresses_list= []

zillow_website_text = requests.get(zillow_website).text
soup = BeautifulSoup(zillow_website_text, 'html.parser')

property_links = soup.find_all('a', class_= 'StyledPropertyCardDataArea-anchor')
for property in property_links:
    link= property.get('href')
    links_list.append(link)

property_prices = soup.find_all('span', class_= 'PropertyCardWrapper__StyledPriceLine')
for property in property_prices:
    price = property.text
    prices_list.append(price.split("/")[0].split("+")[0])

property_addresses= soup.find_all('address')
for property in property_addresses:
    address_name= property.text
    addresses_list.append(address_name.strip())


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Filling forms with acquired data
for i in range(len(links_list)):
    driver.get(google_forms_url)
    time.sleep(1.5)
    input_spaces = driver.find_elements(By.CLASS_NAME, 'whsOnd')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    address_input = input_spaces[0]
    price_input = input_spaces[1]
    link_input = input_spaces[2]

    address_input.send_keys(addresses_list[i])
    price_input.send_keys(prices_list[i])
    link_input.send_keys(links_list[i])
    submit_button.click()
    time.sleep(1)