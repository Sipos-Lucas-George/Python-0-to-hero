"""
    Web Scraping with Beautiful Soup external
"""
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
site_a_tags = soup.select("td.title span.titleline a:not(span span a)")
site_score = soup.find_all(name="span", class_="score")

articles = [(article.getText(), article.get("href")) for article in site_a_tags]
site_score = [int(score.getText().split()[0]) for score in site_score]

index = site_score.index(max(site_score))
print("{}\n{}".format(*articles[index]))
