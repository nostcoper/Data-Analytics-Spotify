from API import *

def __collect_data_from_top_artists(top_artists_json:dict)->list:
    items = top_artists_json['items']
    artists_ids = []

    for item in items[:2]:
        artists_ids.append(item['id'])

    return artists_ids

def __collect_data_from_top_tracks(top_tracks_json:dict)->list:
    items = top_tracks_json['items']
    tracks_ids = []

    for item in items[:3]:
        tracks_ids.append(item['id'])

    return tracks_ids

def collect_data_recommendations(top_artists_json:dict, top_tracks_json:dict)->tuple:
    artists_ids = __collect_data_from_top_artists(top_artists_json)
    tracks_ids = __collect_data_from_top_tracks(top_tracks_json)
    return get_recommendations_json(artists_ids, tracks_ids, 9)

def user_recommendations() -> dict:
    user_recommendations = collect_data_recommendations(get_top_artists_json(), get_top_tracks_json())
    songs = {}
    items = user_recommendations['tracks']
    for item in items:
        info = {}
        info['name'] = item['name']
        info['popularity'] = item['popularity']
        info['id'] = item['id']
        info['images'] = item['album']['images']
        songs[item['name']] = info

    return songs
   
