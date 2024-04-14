import time

import requests
import smtplib
from datetime import datetime

my_email = "matheusbailerdemmer@gmail.com"
password = "kzugfeqnllouqpdl"

#Halmstad
MY_LAT = 56.673969
MY_LONG = 12.857290
def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    print(f"ISS coordinates = {longitude}:{latitude}")
    if (latitude - 5 <= MY_LAT < latitude + 5) and (longitude - 5 <= MY_LONG < longitude + 5):
        print("ISS above")
        return True
    print("ISS isn´t above")
    return False

def iss_visible():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunset_time = int(sunset.split("T")[1].split(":")[0])
    sunrise_time = int(sunrise.split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour <= sunrise_time or time_now.hour >= sunset_time:
        print("The sky is dark")
        return True
    print("The sky is still bright")
    return False

def sendIssEmail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gabriselnem@gmail.com",
                            msg=f"Subject:ISS right above \n\n Look up, it should be visible right now")
    is_iss_above = iss_above()
    is_iss_visible = iss_visible()
    if is_iss_above and is_iss_visible:
        print("Sending email")
        sendIssEmail()
    else:
        print("Not sending email... \n\n")
