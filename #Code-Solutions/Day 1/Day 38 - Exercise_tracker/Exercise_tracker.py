import requests
from datetime import datetime as dt

APP_ID = '13fa58e0'
API_KEY = '0e59c8139326e427882495bc10014fe3'
AUTH_TOKEN = 'ABCD1231231aZCZXF#$1#$#GXHSFADF545'

nutritionix_end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_end_point = 'https://api.sheety.co/5e13990dcd7b5444acaaee22f16c7dff/myWorkouts/workouts'

header_params = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}
user_params= {
    "query": input("What did you to today? "),
}
bearer_headers = {
    'Authorization': 'Bearer ABCD1231231aZCZXF#$1#$#GXHSFADF545'
}

today = dt.now()
today_date = today.strftime('%d/%m/%Y')
current_time = today.strftime("%H:%M:%S")

response= requests.post(url= nutritionix_end_point, json= user_params, headers= header_params)
response.raise_for_status()
data = response.json()

for exercise in data['exercises']:
    exercise_name = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    # Sending data to Google Sheets
    sheety_data = {
    'workout':{
        "date": today_date,
        'time': current_time,
        'exercise': exercise_name,
        'duration': duration,
        'calories': calories
        }
    }
    response = requests.post(url= sheety_end_point, json= sheety_data, headers= bearer_headers)






