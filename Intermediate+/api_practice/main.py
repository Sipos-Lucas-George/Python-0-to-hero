"""
    International Space Station Current Location
    Sunrise/Sunset Exact Time
    Sends Email When ISS is Overhead at Night
"""
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "...@gmail.com"
MY_PASSWORD = "password"
MY_LATITUDE = 47.793301
MY_LONGITUDE = 22.877081


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    position = response.json()["iss_position"]

    iss_latitude = float(position["latitude"])
    iss_longitude = float(position["longitude"])
    return True if abs(iss_latitude - MY_LATITUDE) < 5 and abs(iss_longitude - MY_LONGITUDE) < 5 else False


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, MY_EMAIL, msg=f"Subject:Look Up👆\n\nThe ISS is above you in the sky.")
