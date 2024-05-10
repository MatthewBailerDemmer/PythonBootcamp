#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
USER = "user"
USERNAME = "matheus"
PASSWORD = "password"
FLIGHT_API_KEY = "key"
ACCOUNT_SID = "sid"
AUTH_TOKEN = "auth token"

sheet = DataManager(USER, USERNAME, PASSWORD)
flight_search = FlightSearch(FLIGHT_API_KEY)

cities_list = sheet.get_cities()
cities_codes = flight_search.search_code(cities_list)
sheet.put_cities_codes(cities_codes)
lowest_prices = sheet.get_prices()
search_flights = flight_search.search_flights(cities_codes)

for i in range(len(lowest_prices)):
    for flight in search_flights[i]:
        if lowest_prices[i] > flight["price"]:
            notification = NotificationManager(ACCOUNT_SID, AUTH_TOKEN)
            notification.send_message(flight)



