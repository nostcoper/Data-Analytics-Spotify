
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Token import *


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = RE_DIRECT_URI))

user = sp.current_user()

def get_recently_played_songs(number):
    """Utiliza el método current_user_recently_played() para obtener el nombre de las
       canciones reproducidas recientementes

    Args:
        number (int): número de canciones recientes a obtener

    Returns:
        list: lista de tuplas con el nombre de las canciones reproducidas recientemente
        como primer valor y su id como el segundo
    """
    current_recently_played = sp.current_user_recently_played(number)
    items = current_recently_played['items']
    song_list = []
    for song in items:
        track = song['track']
        song_name = track['name']
        song_id = track['id']
        song_tuple = (song_name, song_id)
        song_list.append(song_tuple)
    return song_list

def get_user_top_tracks(number):
    """Utiliza el método current_user_top_tracks() para obtener el nombre de las canciones
       más reproducidas.

    Args:
        number (int): número de canciones a obtener

    Returns:
        dict: diccionario con el nombre de las canciones como clave y su id como valor
    """
    top_tracks = sp.current_user_top_tracks(number)
    items = top_tracks['items']
    song_dict = {}
    for song in items:
        song_dict[song['name']] = song['id']
    return song_dict
