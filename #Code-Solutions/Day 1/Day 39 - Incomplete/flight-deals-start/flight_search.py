import requests
from datetime import datetime as dt


API_KEY = 'mG1TGJ7kLuYeVnin7AKdRKXmoxX0ZRjb'
API_SECRET = 'QBErmoZUfXNv0b0x'
auth_end_point = 'https://test.api.amadeus.com/v1/security/oauth2/token'
auth_header = {
    "Content-Type": "application/x-www-form-urlencoded",
}
auth_data = {
    'grant_type': 'client_credentials',
    'client_id': API_KEY,
    "client_secret": API_SECRET
}


class FlightSearch:

    def __init__(self) -> None:
        self.token = self.get_access_token()
        self.bearer_header = {
            'Authorization': f'Bearer {self.token}',
            }
        

    def get_access_token(self):
        response = requests.post(auth_end_point, data=auth_data, headers=auth_header)
        response.raise_for_status()
        token = response.json()['access_token']
        return token

    def get_tomorrow_date(self):
        now = str(dt.now())
        formatted_dt = now.split(" ")
        date = formatted_dt[0].split("-")
        date_day = int(date[2])
        tomorrow_day = date_day+1
        date[2] = '0' + str(tomorrow_day)
        tomorrow_date = '-'.join(date)
        return tomorrow_date

    def get_city_IATA(self, city):
        city_params = {
            'keyword': "",
        }
        city_params['keyword'] = city
        city_endpoint = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

        city = requests.get(city_endpoint, city_params, headers=self.bearer_header)
        iata_code = city.json()['data'][0]['iataCode']
        return iata_code


    def get_offers(self, destination ):
        offers_params = {
            'originLocationCode': "LON",
            'destinationLocationCode': destination,
            'departureDate': self.get_tomorrow_date() ,
            'adults': '1',
            'nonStop': 'true',
            'max': 10
        }
        offers_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        offers = requests.get(offers_endpoint, offers_params, headers=self.bearer_header).json()['data']
        return offers
    
flight = FlightSearch()
# city_IATA = flight.get_city_IATA("Paris")
# print(city_IATA)