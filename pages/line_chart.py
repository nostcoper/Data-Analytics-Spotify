import streamlit as st
from data_recolection.data_common_tracks import *

def markdown_song(dict):
    for song in dict.keys():
        name = song
        image = dict[song]['image']['url']
        st.markdown(f'<div class= "artist-list">  <img class="image-artist-list" src="{image}"><h3>{name}</h3> </div>', unsafe_allow_html=True)


def verify_tracks_in_common(top_50):
    common_tracks = []
    top_user = user_top_tracks()
    for general_top, user_top in zip(top_50.keys(), top_user.keys()):
        if general_top == user_top:
            common_tracks.append(top_50[general_top])
    if common_tracks != []:
        for track in common_tracks:
            markdown_song(track)
    else:
        st.markdown(f'<div class="regular-text">¡Eres diferente!</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="regular-text">No tienes nada en común con los top 50 de colombia</div>', unsafe_allow_html=True)