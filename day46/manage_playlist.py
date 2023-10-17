''' Module to authenticate with SpotifyOAuth and provide functions to create a playlist'''
import os
from dotenv import load_dotenv
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Set your Spotify API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
URL_REDIRECT = "http://example.com"
SCOPE = "playlist-modify-private"
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
current_user = sp.current_user()
current_user_id = current_user['id']

def create_playlist(user_id, playlist_name):
    '''return the playlist id'''
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=False
        )
    print(f"Playlist: {playlist_name} id is {playlist['id']}")
    return playlist['id']

def add_to_playlist(user_id, playlist_id, spotify_uris):
    '''add uri tracks to a playlist'''
    new_list = []
    for artist, uri in spotify_uris.items():
        new_list.append(uri)

    response = sp.user_playlist_add_tracks(user_id, playlist_id, tracks=new_list)
    return response
