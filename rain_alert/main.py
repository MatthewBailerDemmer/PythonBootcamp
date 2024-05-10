import requests
from twilio.rest import Client

api_key = "72b5218ab17807c0132ba37db2bc9dae"
lat = 56.673969
lon = 12.857290

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": 56.673969,
    "lon": 12.857290,
    "appid": api_key,
}

account_sid = "KEY"
auth_token = "auth token"

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["hourly"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+12679332335",
        body="Its going to rain today. Remember to bring an ☔",
        to="+447927462101",
    )
    print(message.status)
