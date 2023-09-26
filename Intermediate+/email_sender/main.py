"""
    Send Monday Motivation Emails With smtplib
"""
import smtplib
import datetime as dt
import random

MY_EMAIL = "...@gmail.com"
MY_PASSWORD = "password"
SEND_TO_EMAIL = "...@yahoo.com"
SUBJECT = "Subject:Monday Motivation\n\n"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smpt.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=SEND_TO_EMAIL, msg=SUBJECT+quote)


