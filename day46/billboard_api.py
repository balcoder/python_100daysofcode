'''Scrape Billboard for hot 100 of certain year '''
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.billboard.com/charts/hot-100/"

class ScrapeBillboard:
    '''Scrape billboard website for top 100 songs at a give date'''
    def __init__(self, base_url) -> dict:
        self.base_url = base_url
        self.artists_and_songs_dict = {}

    def check_date(self, date) -> bool:
        '''Make sure date is properly formatted'''
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            return True

        except ValueError:
            print("Date is not in the specified format")
            return False
    def get_artists_songs(self):
        ''' Return a dictionary of top 100 artist:songs for the date provided'''
        date_needs_checking = True
        while date_needs_checking:
            year = input("What year would you like to travel to in YYYY-MM-DD")
            if self.check_date(year):
                date_needs_checking = False
                response = requests.get(f"{BASE_URL}{year}", timeout=30)
                print(response.status_code)
                if response.status_code == 200:
                    webpage = response.text
                    soup = BeautifulSoup(webpage, 'html.parser')
                    rows_artist = soup.select('span.c-label.a-font-primary-s')
                    rows_songs = soup.select('h3#title-of-a-story.a-no-trucate')
                    artists_and_songs_list = zip(rows_artist, rows_songs)

                    for artist, song in artists_and_songs_list:
                        cleaned_song = re.sub(r'\n|\t', '', song.getText())
                        cleaned_artist = re.sub(r'\n|\t', '', artist.getText())
                        self.artists_and_songs_dict[cleaned_artist] = cleaned_song
                    # print(self.artists_and_songs_dict)
                else:
                    print(f"Something wrong with request, error:{response.status_code}")
        return [year, self.artists_and_songs_dict]
