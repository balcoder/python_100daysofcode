"Scrape the web with beautifulsoup and write top 100 movies to file"
import os
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

def get_top_movies(url):
    response = requests.get(URL)
    if response.status_code == 200:
        web_page = response.text
        soup = BeautifulSoup(web_page, 'html.parser')
        movie_list = soup.select('h3.title')
        titles = [movie.getText() for movie in movie_list]
        # titles = []
        # for movie in movie_list:
        #     titles.append(movie.get_text())
        titles.reverse()
        return titles

top_titles = get_top_movies(URL)
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
with open(f"{path}/top_100.txt", "w", encoding="utf-8") as my_file:
    for title in top_titles:
        my_file.write(f"{title}\n")
