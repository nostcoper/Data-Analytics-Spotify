import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
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

#gets recently played songs from the user and returns a dict with the  API data 
def get_recently_played_songs_json()->dict:
    global sp
    return sp.current_user_recently_played(50)

#gets user top artists from the user and returns a dict with the  API data
def get_top_artists_json()->dict:
    global sp
    return sp.current_user_top_artists(50,5,"long_term")

#gets user top tracks from the user and returns a dict with the  API data
def get_top_tracks_json()->dict:
    global sp
    return sp.current_user_top_tracks(50, 5,"long_term")

#gets user liked tracks from the user and returns a dict with the  API data
def get_saved_tracks_json()->dict:
    global sp
    return sp.current_user_saved_tracks(50,5)
