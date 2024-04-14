import requests
import datetime
import os

from requests.auth import HTTPBasicAuth

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
GENDER = "male"
WEIGHT = 115
HEIGHT = 180
AGE = 24
SHEET = "workouts"
PROJECT = "myWorkouts"
USERNAME = os.environ["USERNAME"]
USER = os.environ["USER"]
PASS = os.environ["PASS"]
desc = input("What did you do today?")

header = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
     "query": desc,
     "gender": GENDER,
     "weight_kg": WEIGHT,
     "height_cm": HEIGHT,
     "age": AGE
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=endpoint, headers=header, json=parameters)
response.raise_for_status()
data = response.json()["exercises"]

endpoint = f"https://api.sheety.co/{USERNAME}/myWorkouts/workouts"
date = datetime.datetime.now()

dates = f"{date.strftime("%d")}/{date.strftime("%m")}/{date.strftime("%Y")}"
time = f"{date.strftime("%H")}:{date.strftime("%M")}:{date.strftime("%S")}"

basic = HTTPBasicAuth(USER, PASS)

# headers = {
#     "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"
# }

for exercise in data:
    params = {
        "workout": {
            "date": dates,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=endpoint, json=params, auth=basic)
    response.raise_for_status()
    print(response.status_code)



