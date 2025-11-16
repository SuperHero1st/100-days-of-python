import datetime as dt

now= dt.datetime.now()
today = now.weekday()
days_dict = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

print(days_dict[today])
days_dict