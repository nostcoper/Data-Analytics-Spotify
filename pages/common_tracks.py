import streamlit as st
from API import sp, get_top_tracks_json, get_top_artists_json, get_saved_tracks_json, get_recently_played_songs_json
from data_recolection.pareto_data.collect_data import *
from API import *
from components import items_with_image
from data_recolection.pareto_data.data_common_tracks import top_50_global, top_50_colombia, user_top_tracks, common_tracks
from statistics_processes.pie_chart.processing_pie_data import creates_pie
from data_recolection.pie_data.collect_data import collect_data_for_pie_chart
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
            padding-left: 7rem;
            padding-right: 7rem;
            padding-top: 2rem;
        }
    </style>
"""



st.markdown(margins_css, unsafe_allow_html=True)

artist_dict = get_top_artists_dict(get_top_artists_json())

count_artists_in_top_tracks_json(artist_dict,  get_top_tracks_json())
count_artists_in_recently_played_or_saved_tracks_json(artist_dict, get_recently_played_songs_json())

st.markdown("""
    <style>
        .custom-columns > div {
            margin-right: 50px;
        }
    </style>
    """, unsafe_allow_html=True)

artist_list, separate ,graph = st.columns([15,1,15])

st.container()
with artist_list:
    st.markdown(f'<p class="artist-list-top-global">TOP 50 GLOBAL</p>', unsafe_allow_html=True)
    items_with_image(top_50_global())

    st.markdown(f'<p class="artist-list-top-colombia">TOP 50 COLOMBIA</p>', unsafe_allow_html=True)
    items_with_image(top_50_colombia())
    
    st.markdown(f'<p class="artist-list-top-current">TU TOP</p>', unsafe_allow_html=True)
    items_with_image(user_top_tracks())

with graph:
    st.markdown(f'<div class="separate"> </div>', unsafe_allow_html=True)
    st.markdown(f'<p class="artist-list-common">EN COMÚN CON TOP GLOBAL</p>', unsafe_allow_html=True)
    common_track_global = common_tracks(user_top_tracks(), top_50_global())
    if len(common_track_global) == 0:
        st.markdown('''<div class="container-image-home">
                    <img class="image-common" src="https://play-lh.googleusercontent.com/P2VMEenhpIsubG2oWbvuLGrs0GyyzLiDosGTg8bi8htRXg9Uf0eUtHiUjC28p1jgHzo">
                </div>''', unsafe_allow_html=True)
        
        st.markdown(f'<p class="common-message">!Eres Diferente!</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="common-message">No tienes canciones en común</p>', unsafe_allow_html=True)
    else:
        items_with_image(common_track_global)

    st.markdown(f'<p class="common-message"></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="artist-list-common">EN COMÚN CON TOP COLOMBIA</p>', unsafe_allow_html=True)
    common_track_colombia = common_tracks(user_top_tracks(), top_50_colombia())
    if len(common_track_colombia) == 0:
        st.markdown('''<div class="container-image-home">
                    <img class="image-common" src="https://play-lh.googleusercontent.com/P2VMEenhpIsubG2oWbvuLGrs0GyyzLiDosGTg8bi8htRXg9Uf0eUtHiUjC28p1jgHzo">
                </div>''', unsafe_allow_html=True)
        
        st.markdown(f'<p class="common-message">!Eres Diferente!</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="common-message">No tienes canciones en común</p>', unsafe_allow_html=True)
    else:
        items_with_image(common_track_colombia)

