"""
    Best Flight Deals Using Tequila API
"""
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from subscribe import Subscribe

ORIGIN_CITY_IATA = "BUD"

flight_search = FlightSearch()
data_manager = DataManager(flight_search)
notification_manager = NotificationManager()
subscribe = Subscribe()

destination_data = data_manager.get_destination_data()
# uncomment to update IATA codes
# data_manager.update_destination_codes()
subscribe.subscribe_for_updates()

tomorrow = datetime.now() + timedelta(days=1)
six_months_later = tomorrow + timedelta(days=180)
for city in destination_data:
    flight = flight_search.check_flight(ORIGIN_CITY_IATA, city["iataCode"], tomorrow, six_months_later)
    if flight is None:
        continue
    print(flight)
    if flight.price < city["lowestPrice"]:
        notification_manager.send_notification(subscribe.get_subscribers_email(), flight)
