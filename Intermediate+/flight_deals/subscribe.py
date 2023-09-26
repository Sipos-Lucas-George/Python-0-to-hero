import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/95b898dd22c3af3784d3871248520d01/flightDeals/users"
BEARER = os.getenv("BEARER")


class Subscribe:
    def __init__(self):
        self.__headers = {
            "Authorization": f"Bearer {BEARER}"
        }

    def subscribe_for_updates(self):
        print("Welcome to Lucas' Flight Club.\nWe find the best flight deals and email them to you.")
        first_name = input("What's your first name: ").title()
        last_name = input("What's your last name: ").title()
        email1 = "1"
        email2 = "2"
        while email1 != email2:
            email1 = input("Enter your email: ")
            if email1 == "exit" or email1 == "quit":
                exit()
            email2 = input("Re-enter your email: ")
            if email2 == "exit" or email2 == "quit":
                exit()

        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email1
            }
        }
        response = requests.post(SHEETY_ENDPOINT, json=new_data, headers=self.__headers)
        response.raise_for_status()
        print(response.text)

    def get_subscribers_email(self):
        response = requests.get(SHEETY_ENDPOINT, headers=self.__headers)
        response.raise_for_status()
        return [user["email"] for user in response.json()["users"]]
