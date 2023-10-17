'''Accessing Spotify API using Client Credentials Flow
    The Client Credentials flow is used in server-to-server authentication.
    Only endpoints that do not access user information can be accessed.
    https://spotipy.readthedocs.io/en/2.22.1/#'''
import os
import json
import base64
from  requests import post, get
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
# Set your Spotify API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
URL_REDIRECT = "http://example.com"
SCOPE = "playlist-modify-private"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"


def get_token():
    '''get the access token from spotify'''
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    headers = {
        'Authorization': 'Basic '+ auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    result = post(SPOTIFY_TOKEN_URL, headers=headers, data=data, timeout=20)
    json_result = json.loads(result.content) # convert json string to dict
    token = json_result['access_token']
    return token

def get_auth_header(token):
    ''' return formated header'''
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    '''Get artist info'''
    headers = get_auth_header(access_token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = SPOTIFY_SEARCH_URL + query
    result = get(query_url, headers=headers, timeout=20)
    json_result = json.loads(result.content)['artists']['items'] # convert json string to dict
    if len(json_result) == 0:
        print('No artist with this name exists. Try again')
        return None
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    '''Get a json list of songs by artist id'''
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(access_token)
    result = get(url, headers=headers, timeout=20)
    json_result = json.loads(result.content)
    return json_result

access_token = get_token()
artist_result = search_for_artist(access_token, 'Led Zepplin')
artist_id = artist_result['id']
songs = get_songs_by_artist(access_token, artist_id=artist_id)

for song in songs['tracks']:
    print(song['name'])
