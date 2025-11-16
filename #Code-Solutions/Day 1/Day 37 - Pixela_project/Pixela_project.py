import requests
from datetime import datetime as dt

USERNAME = 'superhero'
TOKEN = "0102203123123#Aa"
graphID = "graph1"
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

graph_config = {
    "id": graphID,
    'name': 'My Gym Graph',
    'unit': "Hours",
    'type': 'float',
    'color': 'momiji',
}
my_headers = {
    "X-USER-TOKEN": TOKEN
}

####### ---->  Creating A Graph  <-------- ######

# grahp_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url= grahp_endpoint, json=graph_config, headers=my_headers )
# print(response.text)

####### ---->  Creating A Pixel  <-------- ######

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"
today= dt.now()

# pixel_config = {
#     'date': today.strftime("%Y%m%d"),
#     'quantity': '1.5',
# }

# response = requests.post(url= pixel_endpoint, json= pixel_config, headers=my_headers )
# print(response.text)

####### ---->  Updating A Pixel  <-------- ######

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{today.strftime('%Y%m%d')}"
update_data = {
    'quantity': '0.5',
}
response = requests.put(url= put_endpoint, json= update_data, headers=my_headers)
print(response.text)
