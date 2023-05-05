#gets the API top artists data as a dict and returns a dict with the artist name and a default value of 0
def get_top_artists_dict(top_artists_json:dict)->dict:
    top_artists_dict = {}
    for artist in top_artists_json['items']:
        top_artists_dict[artist['name']] = 0
    return top_artists_dict

#counts artists in the API top tracks JSON and returns a dict with the artist name and the count
def count_artists_in_top_tracks_json(top_artists_dict:dict, json:dict)->dict:
    for item in json['items']:
        for artist in item['artists']:
            try:
                top_artists_dict[artist['name']] += 1
            except KeyError:
                continue
    return top_artists_dict


#counts artists in the API recently played JSON and returns a dict with the artist name and the count
def count_artists_in_recently_played_or_saved_tracks_json(top_artists_dict:dict, json:dict)->dict:
    for item in json['items']:
        for artist in item['track']['artists']:
            try:
                top_artists_dict[artist['name']] += 1
            except KeyError:
                continue
    return top_artists_dict