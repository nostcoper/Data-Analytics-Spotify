def get_recently_played_songs(current_recently_played):
    """Utiliza el método current_user_recently_played() para obtener el nombre de las
       canciones reproducidas recientementes

    Args:
        current_recently_played (dict): diccionario con la información del usuario

    Returns:
        list: lista de tuplas con el nombre de las canciones reproducidas recientemente
        como primer valor y su id como el segundo
    """
    items = current_recently_played['items']
    song_list = []
    for song in items:
        track = song['track']
        song_name = track['name']
        song_id = track['id']
        song_tuple = (song_name, song_id)
        song_list.append(song_tuple)
    return song_list

def get_user_top_tracks(top_tracks):
    """Utiliza el método current_user_top_tracks() para obtener el nombre de las canciones
       más reproducidas.

    Args:
        current_recently_played (dict): diccionario con la información del usuario

    Returns:
        dict: diccionario con el nombre de las canciones como clave y su id como valor
    """
    items = top_tracks['items']
    song_dict = {}
    for song in items:
        song_dict[song['name']] = song['id']
    return song_dict