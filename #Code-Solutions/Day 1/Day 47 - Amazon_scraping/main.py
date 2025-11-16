import requests, smtplib, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Define the variables using os.getenv
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
product_website = 'https://appbrewery.github.io/instant_pot/'
amazon_website = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'


header= {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9",
}

website = requests.get(product_website, headers=header).text
print(website)
soup = BeautifulSoup(website, 'html.parser')
# print(soup.prettify())

price_whole = soup.select_one('span .a-price-whole')
price_fraction = soup.select_one('span .a-price-fraction')
price = float(price_whole.get_text()) + float(price_fraction.get_text())/100
title = soup.find(class_= 'a-size-large product-title-word-break').get_text()
formatted_title = (" ".join(title.split()))

def send_price_alert():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection :
        connection.starttls()
        connection.login(user= MY_EMAIL, password=MY_PASSWORD)
        message = f"Price Alert! \n\n {title} is now {price}$\n{product_website} ".encode('utf-8')
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= MY_EMAIL,
                            msg=message)

if price<100:
    send_price_alert()