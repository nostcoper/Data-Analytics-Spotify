import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

sp = None

def authorization(client_id, client_secret, redirect_uri):
    global sp
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri , scope= 'user-library-read'))
        user = sp.current_user()
        get_user_info()
        return True, user['display_name']
        
    except:
        return False, ""

def get_user_info():
    global sp
    with open('current_user.json', 'w') as archivo:
        json.dump(sp.current_user(), archivo, indent=4)

    with open('current_user_saved_albums.json', 'w') as archivo:
        json.dump(sp.current_user_saved_albums(), archivo, indent=4)