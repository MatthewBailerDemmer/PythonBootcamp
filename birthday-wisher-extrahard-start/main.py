##################### Extra Hard Starting Project ######################
import pandas

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

def send_birthday_email(letter ,email):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{letter}")




# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
birth_day_dict = data.to_dict("records")
birthday_persons = [item for item in birth_day_dict if item["month"] == now.month and item["day"] == now.day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if birthday_persons:
    letter_list = []
    with open("letter_templates/letter_1.txt") as letter:
        letter_list.append(letter.read())
    with open("letter_templates/letter_2.txt") as letter:
        letter_list.append(letter.read())
    with open("letter_templates/letter_3.txt") as letter:
        letter_list.append(letter.read())
    for i in range(len(birthday_persons)):
        letter = random.choice(letter_list)
        letter = letter.replace("[NAME]", birthday_persons[i]["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        send_birthday_email(letter, birthday_persons[i]["email"])

