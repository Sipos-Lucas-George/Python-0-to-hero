"""
    Stock News For Prices >|5%| Daily
"""
import requests
import smtplib
import os


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = os.environ.get("STOCK_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_EMAIL = "...@gmail.com"
MY_PASSWORD = "password"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}
response_stock = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response_stock.raise_for_status()
data_100_days = response_stock.json()["Time Series (Daily)"]
last_2_days = []
for index, (key, value) in enumerate(data_100_days.items()):
    if index > 1:
        break
    last_2_days.append(value)
yesterday = float(last_2_days[0]["4. close"])
before_yesterday = float(last_2_days[1]["4. close"])
difference = abs(yesterday - before_yesterday)
average = (yesterday + before_yesterday) / 2
percentage = difference / average * 100
if percentage > 5:
    percentage_details = ("🔺" if yesterday > before_yesterday else "🔻") + str(round(percentage, 2)) + "%"
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_KEY
    }
    response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    data_first_3_news = response_news.json()["articles"][:3]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for item in data_first_3_news:
            connection.sendmail(MY_EMAIL, MY_PASSWORD, msg=f"Subject:{STOCK_KEY}: {percentage_details}\n\n"
                                                           f"Headline:{item['title']}"
                                                           f"Brief:{item['description']}")
