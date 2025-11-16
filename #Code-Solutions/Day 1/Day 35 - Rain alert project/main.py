import requests
from twilio.rest import  Client

account_sid = 'AC39ff7f95bba90ff9c9c92bfd328f2176'
auth_token = '17efb4ba12db7e40664c802b4fe8fdb4'

api_key= "7d9c9ff0b20340f4a5009fc9a0295432"
MY_LAT = 30.784451
MY_LONG = 30.997881

params= {
    'lat': {MY_LAT},
    'lon': {MY_LONG},
    'appid': {api_key},
    "cnt": 4,
}
response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast', params)
response.raise_for_status()
question_data = response.json()

weather_desc = question_data['list'][0]["weather"][0]["description"]
weather_id = question_data['list'][0]["weather"][0]["id"]


for day in question_data['list']:
    if day["weather"][0]["id"] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= "It's going to rain today. Bring an ☔☔.",
            from_="whatsapp:+14155238886",
            to="whatsapp:+201026036133"
        )
        print(message.status)
        break



client = Client(account_sid, auth_token)