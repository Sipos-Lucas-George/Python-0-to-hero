import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
titles = [title_tag.getText() for title_tag in soup.find_all("h3", class_="title")]
titles = titles[::-1]

with open("movies.txt", "w") as file:
    for title in titles:
        file.write(title + "\n")
