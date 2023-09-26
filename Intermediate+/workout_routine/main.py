"""
    Workout Routine Using Natural Language Engine (nutritionix)
"""
import requests
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/95b898dd22c3af3784d3871248520d01/myWorkout/workouts"
TOKEN = os.getenv("TOKEN")
ID = os.getenv("ID")
BEARER = os.getenv("BEARER")

query = input("What did you do today: ")

nutritionix_headers = {
    "x-app-id": ID,
    "x-app-key": TOKEN,
    "Content-Type": "application/json",
}
nutritionix_parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 165,
    "age": 21
}
nutritionix_response = requests.post(EXERCISE_ENDPOINT, headers=nutritionix_headers, json=nutritionix_parameters)
nutritionix_response.raise_for_status()
data = nutritionix_response.json()["exercises"]
print(data)
sheety_headers = {
    "Authorization": f"Bearer {BEARER}"
}
for exercise in data:
    sheety_parameters = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration (min)": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    print(sheety_response.text)
