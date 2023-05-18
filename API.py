import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tokens import *

sp = None
SCOPE = ['user-library-read','user-top-read','user-read-recently-played']

def authorization(client_id, client_secret, redirect_uri):
    global sp
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri , scope= SCOPE))
        user = sp.current_user()
        return True, user['display_name']   
    except:
        return False, ""

def get_top_tracks_json(cant)->dict:
    global sp
    return sp.current_user_top_tracks(cant,5,"long_term")


def get_recently_played_songs_json()->dict:
    global sp
    return sp.current_user_recently_played(50)

def get_track(id) -> dict:
    global sp
    return sp.track(id)

authorization(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)