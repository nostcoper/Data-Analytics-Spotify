import os
from API import *
import streamlit as st
from statistics_processes.line_chart.making_line_chart import *
from statistics_processes.pie_chart.processing_pie_data import creates_pie
from data_recolection.pie_data.collect_data import collect_data_for_pie_chart
from API import sp, get_top_tracks_json, get_top_artists_json, get_saved_tracks_json, get_recently_played_songs_json

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

st.markdown(f'<p class="message-popularity"> Gráfica tu top de artistas más escuchados</p>', unsafe_allow_html=True)
st.write("-----")
col1, col2, col3 = st.columns(3)

data = collect_data_for_pie_chart(get_top_artists_json(), get_top_tracks_json(), get_recently_played_songs_json(), get_saved_tracks_json())
chart = creates_pie (data)
with col2:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)