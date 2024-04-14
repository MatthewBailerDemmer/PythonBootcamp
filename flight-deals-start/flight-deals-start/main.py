#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
USER = "1cb2f60f32c7e6b85c85ee8fe606232c"
USERNAME = "matheus"
PASSWORD = "Cogumelos1@"
FLIGHT_API_KEY = "Wai3aD71bWuH_2mTGQgVyjDmv6Rjs-nM"
ACCOUNT_SID = "AC3bd1d9b23ff95534f7212e524abd3b36"
AUTH_TOKEN = "efc8808667bdb9ae790729df0d07da5a"

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



