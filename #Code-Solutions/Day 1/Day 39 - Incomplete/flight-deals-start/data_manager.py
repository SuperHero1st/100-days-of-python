import requests

END_POINT = f'https://api.sheety.co/5e13990dcd7b5444acaaee22f16c7dff/flightDeals/prices/'
Bearer_header = {
    'Authorization': 'Bearer elstmde7a_a7a555asdav#$#$',
    'Content-Type': 'application/json'
}


class DataManager:
    def __init__(self):
        self.data = {
        'price':{
            'iataCode': "",
            }
        }


    def update_iata(self, row_num, IATA_code):
        self.data ['price']['iataCode'] = IATA_code
        new_endpoint = END_POINT + str(row_num)
        self.response = requests.put(new_endpoint, headers=Bearer_header, json= self.data)


    def get_city_names(self):
        cities = []
        data = requests.get(END_POINT, headers= Bearer_header).json()
        for i in range (len(data['prices'])):
            cities.append(data['prices'][i]['city'])
        return cities
    
    
    def check_iata_column(self):
        response = requests.get(END_POINT, headers=Bearer_header)
        response = response.json()
        iata_column = response['prices'][0]['iataCode']
        if iata_column:
            return True
        return False
    

    def get_IATAs(self):
        response = requests.get(END_POINT, headers=Bearer_header).json()
        iata_codes = []
        for row in response['prices']:
            code = row['iataCode']
            iata_codes.append(code)
        return iata_codes


    def get_sheet_data(self):
        return requests.get(END_POINT, headers= Bearer_header).json()



# datamanager.update_iata('2', 'PAR')