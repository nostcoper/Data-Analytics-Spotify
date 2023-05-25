import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from API import get_top_artists_json_cloud, get_top_tracks_json_cloud


def trigger_wordcloud(genres: list):
    genres = ' '.join(genres)
    fig, ax = plt.subplots()
    wordcloud = WordCloud().generate(genres)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    return fig

def wordcloud_info() -> list:
    user_top = get_top_artists_json_cloud(50,"long_term")
    genres = [] 
    items = user_top['items']
    for item in items:
        genres.extend(item['genres'])

    return genres