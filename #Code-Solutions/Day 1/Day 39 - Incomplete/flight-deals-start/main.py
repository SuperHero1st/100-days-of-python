#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

my_DM = DataManager()
my_FS = FlightSearch()
my_FD = FlightData()
my_NM = NotificationManager()

cities = my_DM.get_city_names()
row_num = 2

if my_DM.check_iata_column() == False:
    for city in cities:
        iata = my_FS.get_city_IATA(city)
        my_DM.update_iata(row_num, iata)
        row_num += 1

iata_codes = my_DM.get_IATAs()

row_num = 2
for code, city in zip(iata_codes, cities):
    print(f"Getting flights for {city}")
    offers = my_FS.get_offers(code)
    min_price = my_FD.struct_offers(offers)
    my_NM.check_price(min_price, row_num)
    row_num += 1

