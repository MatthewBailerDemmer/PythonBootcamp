import requests
import datetime
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = f"https://api.tequila.kiwi.com/"
        self.headers = {
            "apikey": self.api_key,
            "Content-Type": "application/x-www-form-urlencoded"
        }


    def search_code(self, cities: list):
        endpoint = self.endpoint + "locations/query"
        cities_codes = []
        for city in cities:
            params = {
                "term": city
            }
            response = requests.get(url=endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()["locations"][0]["code"]
            cities_codes.append(data)
        return cities_codes

    def search_flights(self, cities_codes: list):
        endpoint = self.endpoint + "v2/search"

        six_months = int(datetime.datetime.now().strftime("%m")) + 6
        to_month = str(six_months)
        if six_months < 10:
            to_month = f"0{to_month}"
        in_six_months = f"{datetime.datetime.now().strftime("%d")}/{to_month}/{datetime.datetime.now().strftime("%Y")}"

        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime("%d/%m/%Y")
        flight_list = []
        for code in cities_codes:
            params = {
                "fly_from": "LON",
                "fly_to": code,
                "date_from": str(tomorrow),
                "date_to": str(in_six_months)
            }
            response = requests.get(url=endpoint, params=params, headers=self.headers)
            response.raise_for_status()
            data = [{"departure_city": flight["cityFrom"],
                     "departure_airport": flight["flyFrom"],
                     "destination_city": flight["cityTo"],
                     "destination_airport": flight["flyTo"],
                     "price": flight["price"],
                     "date_to": flight["utc_arrival"][:9],
                     "date_from": flight["utc_departure"][:9]}for flight in response.json()["data"]]
            flight_list.append(data)
        return flight_list



