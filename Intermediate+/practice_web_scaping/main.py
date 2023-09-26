"""
    Web Scraping with Beautiful Soup local
"""
from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

anchor_tags = soup.find_all(name="a")
anchor_text = [tag.getText() for tag in anchor_tags]
anchor_link = [tag.get("href") for tag in anchor_tags]

heading = soup.find(name="h1", id="name")

section_heading = soup.find(name="h3", class_="heading")

company_url = soup.select_one(selector="p a")

name = soup.select_one(selector="#name")

headings = soup.select(selector=".heading")
