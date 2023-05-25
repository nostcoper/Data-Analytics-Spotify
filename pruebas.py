import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from API import get_top_artists_json, authorization

authorization(
    'your client id',
    'your client secret',
    'http://localhost:8080'
)


def trigger_wordcloud(genres: list):
    genres = ' '.join(genres)
    fig, ax = plt.subplots()
    wordcloud = WordCloud().generate(genres)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def wordcloud_info() -> list:
    user_top = get_top_artists_json(50,"long_term")
    genres = [] 
    items = user_top['items']
    for item in items:
        genres.extend(item['genres'])

    return genres

genres = wordcloud_info()
trigger_wordcloud(genres)