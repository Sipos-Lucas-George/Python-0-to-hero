import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_KEY")


class FlightSearch:
    def __init__(self):
        self.__headers = {
            "apikey": TEQUILA_API_KEY,
        }

    def get_destination_codes(self, city_name):
        parameters = {
            "term": city_name,
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=parameters, headers=self.__headers)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def check_flight(self, origin_city_code, destination_city_code, date_from, date_to):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 14,
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "EUR",
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=self.__headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            parameters["max_stopovers"] = 1
            response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=self.__headers)

            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}.\n")
                return None

            return FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                airline=" / ".join(data["airlines"]),
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )

        return FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            airline=" / ".join(data["airlines"]),
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
