# import smtplib
#
my_email = "matheusbailerdemmer@gmail.com"
password = "password"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="gabriselnem@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

import datetime as dt
import random
import smtplib
now = dt.datetime.now()
day_of_the_week = now.weekday()
new_day = dt.datetime(year=2024, month=2, day=27, hour=4)
day_of_the_week = new_day.weekday()
if day_of_the_week == 1:
    with open("quotes.txt") as file:
        data = file.read()
        quotes = data.split("\n")
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gabriselnem@gmail.com",
                            msg=f"Subject:Moday Inspirational Quote\n\n{quote}")


