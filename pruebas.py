import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from API import get_top_tracks_json

def trigger_wordcloud(genres: list):
    genres = ' '.join(genres)
    fig, ax = plt.subplots()
    wordcloud = WordCloud().generate(genres)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

user_top = get_top_tracks_json(50)
items = user_top['items']
for item in items:
    album = item['album']
    print(album['genres'])
    print('*')