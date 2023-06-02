def __collect_data_from_top_artists(top_artists_json:dict)->list:
    items = top_artists_json['items']
    artists_ids = []

    for item in items:
        artists_ids.append(item['name'])

    return artists_ids

def __collect_data_from_top_tracks(top_tracks_json:dict)->list:
    items = top_tracks_json['items']
    tracks_ids = []

    for item in items:
        tracks_ids.append(item['name'])

    return tracks_ids

def collect_data_for_recommendations(top_artists_json:dict, top_tracks_json:dict)->tuple:
    artists_ids = __collect_data_from_top_artists(top_artists_json)
    tracks_ids = __collect_data_from_top_tracks(top_tracks_json)

    return artists_ids, tracks_ids



