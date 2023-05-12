import streamlit as st
from API import sp, get_top_tracks_json
from data_recolection.pareto_data.collect_data import *
from API import *
from components import items_with_image
from data_recolection.pareto_data.data_common_tracks import top_50_global, top_50_colombia
import os

st.set_page_config(
    page_title="Data Analytics Spotify",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ruta_css = os.path.join(os.getcwd(), "style.css")
with open(ruta_css) as f:
    css = '<style>{}</style>'.format(f.read())
    st.markdown(css, unsafe_allow_html=True)

margins_css = """
    <style>
        .main > div {
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
"""



st.markdown(margins_css, unsafe_allow_html=True)

display_name = sp.current_user()['display_name']
st.markdown(f'<p class="message-home"> Bienvenido {display_name}</p>', unsafe_allow_html=True)

artist_dict = get_top_artists_dict(get_top_artists_json())

count_artists_in_top_tracks_json(artist_dict,  get_top_tracks_json())
count_artists_in_recently_played_or_saved_tracks_json(artist_dict, get_recently_played_songs_json())
artist_list, graph = st.columns(2)

with artist_list:
    st.markdown(f'<p class="artist-list-title">TOP 50 GLOBAL</p>', unsafe_allow_html=True)
    with st.expander("Ver"):
        items_with_image(top_50_global())

    st.markdown(f'<p class="artist-list-title">TOP 50 COLOMBIA</p>', unsafe_allow_html=True)
    with st.expander("Ver"):
        items_with_image(top_50_colombia())