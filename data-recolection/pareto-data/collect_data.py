import json
#gets the JSON top artists data from the user-json folder
def get_top_artists_json()->dict:
    with open('user-json/user_top_artists.json', 'r') as archivo:
        return json.load(archivo)

