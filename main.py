from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles.reverse()

with open("top_100_movies.txt", "w",encoding="utf-8") as file:
    for title in titles:
        file.write(title.text+"\n")