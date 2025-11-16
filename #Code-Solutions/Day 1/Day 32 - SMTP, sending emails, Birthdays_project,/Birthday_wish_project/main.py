import pandas as pd
import smtplib
import random
import datetime as dt

my_email = "ahmedsaidmeod@gmail.com"
my_password = "hnkscojuqgdueeqz"

def send_birthday_wishes(letter, email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection :
        connection.starttls()
        connection.login(user= my_email, password=my_password)
        connection.sendmail(from_addr= my_email,
                            to_addrs= email,
                            msg=f"Subject:Happy Birthday\n\n{letter}")

def write_letter(name):
    # Read the file content
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", 'r') as file:
        letter = file.read()    
    return letter.replace('[NAME]', name)

now= dt.datetime.now()
today = now.day
todays_month = now.month

file = pd.read_csv("birthdays.csv")
birthdays = []
### Collecting Birthdays from the csv ###
for i in range(len(file)):
    row_data = file.loc[i, ['month', 'day']].tolist()
    birthdays.append(row_data)

### Checking for birthdays and sending emails ###
for index, birthday in enumerate(birthdays):
    if birthday[0] == todays_month and birthday[1] ==today:
        name = file.iat[index, file.columns.get_loc('name')]
        email = file.iat[index, file.columns.get_loc('email')]
        my_letter = write_letter(name)
        send_birthday_wishes(my_letter, email)

