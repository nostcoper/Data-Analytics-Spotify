#gets the API top artists data as a dict and returns a dict with the artist name and a default value of 0
def __get_top_artists_dict(top_artists_json:dict)->dict:
    top_artists_dict = {}
    for artist in top_artists_json['items'][:10]:
        top_artists_dict[artist['name']] = 0
    return top_artists_dict

#counts artists in the API top tracks JSON and returns a dict with the artist name and the count
def __count_artists_in_top_tracks_json(top_artists_dict:dict, json:dict)->dict:
    for item in json['items']:
        for artist in item['artists']:
            try:
                top_artists_dict[artist['name']] += 1
            except KeyError:
                continue
    return top_artists_dict


#counts artists in the API recently played JSON and returns a dict with the artist name and the count
def __count_artists_in_recently_played_or_saved_tracks_json(top_artists_dict:dict, json:dict)->dict:
    for item in json['items']:
        for artist in item['track']['artists']:
            try:
                top_artists_dict[artist['name']] += 1
            except KeyError:
                continue
    return top_artists_dict

def __remove_unheard_artists(top_artists_dict:dict):
    top_artists_dict_aux = top_artists_dict.copy()
    
    for artist in top_artists_dict_aux.keys():
        if top_artists_dict[artist] == 0:
            del top_artists_dict[artist]
    
    return top_artists_dict

def collect_data_for_pie_chart(top_artists_json:dict, top_tracks_json:dict,recently_played_json:dict,saved_tracks_json:dict)->dict:
    top_artists_dict = __get_top_artists_dict(top_artists_json)
    top_artists_dict = __count_artists_in_top_tracks_json(top_artists_dict, top_tracks_json)
    top_artists_dict = __count_artists_in_recently_played_or_saved_tracks_json(top_artists_dict, recently_played_json)
    top_artists_dict = __count_artists_in_recently_played_or_saved_tracks_json(top_artists_dict, saved_tracks_json)
    top_artists_dict = __remove_unheard_artists(top_artists_dict)

    return top_artists_dict