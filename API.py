import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

sp = None
SCOPE = ['user-library-read','user-top-read','user-read-recently-played']

def authorization(client_id, client_secret, redirect_uri):
    global sp
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri , scope= SCOPE))
        user = sp.current_user()
        get_user_info()
        return True, user['display_name']
        
    except:
        return False, ""

def get_user_info()->None:
    global sp
    with open('user-json/current_user.json', 'w') as archivo:
        json.dump(sp.current_user(), archivo, indent=4)

    with open('current_user_saved_albums.json', 'w') as archivo:
        json.dump(sp.current_user_saved_albums(), archivo, indent=4)

def get_recently_played_songs_json()->None:
    global sp
    with open('user-json/recently_played_songs.json', 'w') as archivo:
        json.dump(sp.current_user_recently_played(50), archivo, indent=4)

def get_user_top_artists()->None:
    global sp
    with open('user-json/user_top_artists.json', 'w') as archivo:
        json.dump(sp.current_user_top_artists(50,5,"long_term"), 
                  archivo, indent=4)

def get_user_top_tracks()->None:
    global sp
    with open('user-json/user_top_tracks.json', 'w') as archivo:
        json.dump(sp.current_user_top_tracks(50,5,"long_term"), 
                  archivo, indent=4)

def get_user_liked_tracks()->None:
    global sp
    with open('user-json/user_liked_tracks.json', 'w') as archivo:
        json.dump(sp.current_user_saved_tracks(50,5), 
                  archivo, indent=4)