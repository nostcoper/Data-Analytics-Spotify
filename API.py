import spotipy
from spotipy.oauth2 import SpotifyOAuth

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
def get_top_artists_json(limit:int = 50, offset:int = 0,time_range:str="short_term")->dict:
    global sp
    return sp.current_user_top_artists(limit, offset, time_range)

#gets user top tracks from the user and returns a dict with the  API data
def get_top_tracks_json(limit:int = 50, offset:int = 0,time_range:str="short_term")->dict:
    global sp
    return sp.current_user_top_tracks(limit, offset, time_range)


def get_top_tracks_json_cloud(cant)->dict:
    global sp
    return sp.current_user_top_tracks(cant,5,"long_term")

def get_top_artists_json_cloud(cant,time_range:str)->dict:
    global sp
    return sp.current_user_top_artists(cant,0,time_range)

#gets user liked tracks from the user and returns a dict with the  API data
def get_saved_tracks_json()->dict:
    global sp
    return sp.current_user_saved_tracks(50,5)

def get_recommendations_json(artists_ids:list, tracks_ids:list,limit:int)->dict:
    global sp
    return sp.recommendations(seed_artists=artists_ids, seed_tracks=tracks_ids, limit=limit)