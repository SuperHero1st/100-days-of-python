import smtplib
import random
import datetime as dt

days_dict = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
my_email = "ahmedsaidmeod@gmail.com"
my_password = "hnkscojuqgdueeqz"


def send_quote():
    with open(file="quotes.txt", mode="r") as quotes:
        lines = [line.strip() for line in quotes.readlines()]
        random_quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection :
        connection.starttls()
        connection.login(user= my_email, password=my_password)
        connection.sendmail(from_addr= my_email,
                            to_addrs= 'ahmed_saidmedo@yahoo.com',
                            msg=f"Subject:Monday's quote\n\n{random_quote}")

now= dt.datetime.now()
today = 0                 #now.weekday()
if days_dict[today] =="Monday":
    send_quote()


