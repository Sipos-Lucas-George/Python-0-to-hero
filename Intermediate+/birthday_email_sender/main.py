"""
    Birthday Wish Email Sender using smtplib
"""
import datetime as dt
import pandas
import smtplib
from random import randint


MY_EMAIL = "...@gmail.com"
MY_PASSWORD = "password"

today = dt.datetime.now()
today = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(value["month"], data["day"]): data for index, value in data.iterrows()}

if today in birthdays_dict:
    path = f"./letter_templates/letter_{randint(1,3)}.txt"
    with open(path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthdays_dict[today]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthdays_dict[today]["email"],
                            msg=f"Subject:Happy Birthday\n\n{content}")
