from API import *

def create_dict_top_tracks(top_50):
    popularity = {}
    for item in top_50:
        info = {}
        track = item['track']
        info['name'] = track['name']
        info['popularity'] = track['popularity']
        info['id'] = track['id']
        info['images'] = track['album']['images']
        popularity[track['name']] = info
    return popularity


def user_top_tracks() -> dict:
    top_tracks = get_top_tracks_json(50)
    songs = {}
    items = top_tracks['items']
    for item in items:
        info = {}
        info['popularity'] = item['popularity']
        info['id'] = item['id']
        info['image'] = item['album']['images'][1]
        songs[item['name']] = info
    return songs

def top_50_colombia() -> dict:
    tracks_colombia = sp.playlist('37i9dQZEVXbOa2lmxNORXQ')['tracks']['items']
    popularity = create_dict_top_tracks(tracks_colombia)
    return popularity

def top_50_global() -> dict:
    tracks_global = sp.playlist('37i9dQZEVXbMDoHDwVN2tF')['tracks']['items']
    popularity = create_dict_top_tracks(tracks_global)
    return popularity
