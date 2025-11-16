import requests
import itertools
from twilio.rest import Client

account_sid = 'AC39ff7f95bba90ff9c9c92bfd328f2176'
auth_token = '17efb4ba12db7e40664c802b4fe8fdb4'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AlphaVantage_api_key = "NH6VEXKUD02NDVWH"
news_key = '3da5d9e3dea5402b9b61f256281b9dac'

params = {'function': 'TIME_SERIES_DAILY',
          'symbol':  STOCK,
          'apikey': AlphaVantage_api_key,
}
news_params= {
    'apiKey': news_key,
    'q': f"{COMPANY_NAME} News",
    'qInTitle': COMPANY_NAME,
    'pageSize': 3
}

stock_data = requests.get('https://www.alphavantage.co/query', params)
stock_data.raise_for_status()

data = stock_data.json()
meta_data = next(iter(data.items()))
data_list = [value for (key, value) in meta_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_price)
# difference = 2.43
# yesterday_closing_price = 22

up_down = None
if difference > 2:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent= round((difference / float(yesterday_closing_price))* 100) 
print(diff_percent)

if diff_percent >10:
    news = requests.get('https://newsapi.org/v2/everything', news_params)
    news.raise_for_status()
    news_data = news.json()
    three_articles = news_data['articles'][:3]
    formatted_articles = [f"{STOCK}:{up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
        body= article,
        from_="whatsapp:+14155238886",
        to="whatsapp:+201026036133"
    )
        print(message.status)
    
