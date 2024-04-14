from requests.auth import HTTPBasicAuth
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, user: str, username: str, password: str):
        self.user = user
        self.username = username
        self.password = password
        self.endpoint = f"https://api.sheety.co/{user}/flightDeals/prices"
        self.basic = HTTPBasicAuth(username, password)


    def get_cities(self):
        response = requests.get(url=self.endpoint, auth=self.basic)
        response.raise_for_status()
        data = [name["city"] for name in response.json()["prices"]]
        return data

    def get_prices(self):
        response = requests.get(url=self.endpoint, auth=self.basic)
        response.raise_for_status()
        data = [price["lowestPrice"] for price in response.json()["prices"]]
        return data


    def put_cities_codes(self, cities_codes):
        for i in range(len(cities_codes)):
            params = {
                "price": {
                    "iataCode": cities_codes[i]
                }
            }
            response = requests.put(url=self.endpoint + f"/{i + 2}", json=params, auth=self.basic)
            response.raise_for_status()



