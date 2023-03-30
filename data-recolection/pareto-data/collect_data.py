import json
#gets the JSON top artists data from the user-json folder
def get_top_artists_json()->dict:
    with open('user-json/user_top_artists.json', 'r') as archivo:
        return json.load(archivo)

#opens the JSON top artists data and returns a dict with the artist name and a default value of 0
def get_top_artists_dict()->dict:
    top_artists_json = get_top_artists_json()
    top_artists_dict = {}
    for artist in top_artists_json['items']:
        top_artists_dict[artist['name']] = 0
    return top_artists_dict