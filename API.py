import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tokens import *


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = RE_DIRECT_URI))

user = sp.current_user()

