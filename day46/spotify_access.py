'''Use OAuth to authenticate with spotify. Only have to run this once and 
    it saves a token to .cache on parent directory'''
import os
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

# Initialize the SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URL_REDIRECT, scope=SCOPE)


# Get the authorization URL
auth_url = sp_oauth.get_authorize_url()

# Print the authorization URL, open it in a web browser, and follow the instructions
print("Please visit this URL to authorize your application: " + auth_url)

# After authorization, paste the URL you were redirected to in your web browser
auth_response = input("Enter the URL you were redirected to: ")

# # Get the access token and refresh token
# token_info = sp_oauth.get_access_token(auth_response)
# access_token = token_info['access_token']

# # Now you can use the `access_token` to make requests to the Spotify API
# print(f"Access token: {access_token}")
