'''Scrape Billboard for hot 100 of certain year '''
import os
from dotenv import load_dotenv
from billboard_api import ScrapeBillboard
import search_spotify
import manage_playlist

load_dotenv()
# Set your Spotify API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
URL_REDIRECT = "http://localhost:8080/"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search?"

BASE_URL = "https://www.billboard.com/charts/hot-100/"

SCRAPE_BILLBOARD = ScrapeBillboard(BASE_URL)

# ask user for date to get top 100 and return list with year and dict
artists_and_songs = SCRAPE_BILLBOARD.get_artists_songs()

# get the URI's of the songs
my_uris = search_spotify.get_song_uris(artists_and_songs[1])

year = artists_and_songs[0]
playlist_name = f"{year} Billboard 100"

# create a playlist
playlist_id = manage_playlist.create_playlist(manage_playlist.current_user_id, playlist_name)
response = manage_playlist.add_to_playlist(manage_playlist.current_user_id, playlist_id, my_uris)

if response['snapshot_id']:
    print(f"All good, playlist created with snapshot_id of : {response['snapshot_id']}")
else:
    print("Something went wrong wiht the request")

