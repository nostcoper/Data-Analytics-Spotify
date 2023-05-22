def __collect_data_from_top_artists(top_artists_json:dict)->tuple:
    items = top_artists_json['items']
    artists_ids = []
    artists_genres = []

    for item in items:
        artists_ids.append(item['id'])
        artists_genres.append(item['genres'][0])

    return artists_ids, artists_genres

def __collect_data_from_top_tracks(top_tracks_json:dict)->list:
    items = top_tracks_json['items']
    tracks_ids = []

    for item in items:
        tracks_ids.append(item['id'])

    return tracks_ids

def collect_data_for_recommendations(top_artists_json:dict, top_tracks_json:dict)->tuple:
    artists_ids, artists_genres = __collect_data_from_top_artists(top_artists_json)
    tracks_ids = __collect_data_from_top_tracks(top_tracks_json)

    return artists_ids, artists_genres, tracks_ids


