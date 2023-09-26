import requests
import os
from dotenv import load_dotenv
from flight_search import FlightSearch

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/95b898dd22c3af3784d3871248520d01/flightDeals/prices"
BEARER = os.getenv("BEARER")


class DataManager:
    def __init__(self, flight_search: FlightSearch):
        self.destination_data = {}
        self.__headers = {
            "Authorization": f"Bearer {BEARER}"
        }
        self.__flight_search = flight_search

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=self.__headers)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": self.__flight_search.get_destination_codes(city["city"])
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, headers=self.__headers)
            response.raise_for_status()
