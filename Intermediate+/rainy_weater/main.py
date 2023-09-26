"""
    Rainy Weather Alert Next 12 Hours (use twilio to send messages if rainy)
"""
import requests
import smtplib
import os

API_KEY = os.environ.get("API_KEY")
MY_LATITUDE = 47.793301
MY_LONGITUDE = 22.877081
MY_EMAIL = "...@gmail.com"
MY_PASSWORD = "password"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_date = response.json()["list"]

need_umbrella = False
for item in weather_date[:4]:
    for weather in item["weather"]:
        if weather["id"] < 700:
            need_umbrella = True
            break
    if need_umbrella:
        break

if need_umbrella:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_PASSWORD, msg=f"Subject:Weather\n\nBring an umbrella!")
