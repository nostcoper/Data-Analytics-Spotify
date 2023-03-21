#"C:\Users\ASUS\Desktop\2023-1\Electiva de programación\ProyectoAPI\Data-Analytics-Spotify"
#venv\Scripts\activate.bat


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='CLIENT_ID',
                                               client_secret='CLIENT_SECRET',
                                               redirect_uri='http://localhost:1234',
                                               scope="user-library-read"))


def imprimir_canciones_playlist(codigo_playlist):
    #sp.playlist_items('6AdmUjj4BSkN5aPCb5lRnT')
    #Las llaves son: href, items, limit, next, offset, previous, total
    canciones = sp.playlist_items(codigo_playlist)['items']
    for cancion in canciones:
        track = cancion['track']
        print(track['name'])

def artistas_relacionados(codigo_artista):
    #spotify:artist:code
    artistas = sp.artist_related_artists(codigo_artista)['artists']
    for i in artistas:
        artista = i
        nombre = artista['name']
        print(nombre)
    
def mostrar_albumes_artista(codigo_artista):
    #spotify:artist:code
    results = sp.artist_albums(codigo_artista, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])