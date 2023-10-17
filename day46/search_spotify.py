''' Module to authenticate with SpotifyOAuth and provide functions to return single uri given a
    song and artist and dict of uris given a dict of artist:song'''
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Set your Spotify API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
URL_REDIRECT = "http://example.com"
# SCOPE = "playlist-modify-private"
SCOPE = "user-library-read"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SEARCH_ENDPOINT = "https://api.spotify.com/v1/search"



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=URL_REDIRECT,
        scope=SCOPE
    )
)

def get_song_uri(artist, track_name):
    '''return song URI or None'''
    result = sp.search(q=f"artist:{artist} track:{track_name}", type='track')
    if result['tracks']['items']:
        return result['tracks']['items'][0]['uri']
    else:
        return None

def get_song_uris(artists_and_songs):
    '''return a dict of song uris'''
    uri_dict = {}
    for artist, song in artists_and_songs.items():
        uri = get_song_uri(artist, song)
        if uri:
            uri_dict[song] = uri
    return uri_dict

def get_playlist_id(playlist_name):
    result = sp.search(q=f"artist:{artist} track:{track_name}", type='playlist')
    if result['tracks']['items']:
        return result['tracks']['items'][0]['uri']
    else:
        return None