from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), )
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
captcha = driver.find_element(By.LINK_TEXT, "Try different image")
captcha.click()
 
price_whole = driver.find_element(By.CLASS_NAME,"a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME,"a-price-fraction")
print(f"The Price is {price_whole.text}.{price_cents.text}$")

input("Press Enter to close the browser...")
driver.quit()       # Close the browser (only when Enter is pressed)

link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a') # css_selector
driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[4]/table/tbody/tr[1]/td[1]/a')
