import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from API import get_top_tracks_json, get_track, get_album

def trigger_wordcloud(genres: list):
    genres = ' '.join(genres)
    fig, ax = plt.subplots()
    wordcloud = WordCloud().generate(genres)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def wordcloud_info() -> list:
    user_top = get_top_tracks_json(50)
    tracks_artists = [] 
    items = user_top['items']
    for item in items:
        album = item['album']
        artists = album['artists']
        for artist in artists:
            name = artist['name']
            tracks_artists.append(name)
    return tracks_artists

album = get_album('4O3yvEN5II2yKWKBPtDLD7')
print(album['genres'])
#tracks_artists = wordcloud_info()
#trigger_wordcloud(tracks_artists)