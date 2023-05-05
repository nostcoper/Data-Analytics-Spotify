import streamlit as st
from page_config import set_page_config, set_second_pages_title
from data_recolection.data_common_tracks import *
from API import *
from statistics_processes.common_tracks import *

set_page_config()
set_second_pages_title(sp)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<p class="artist-list-title">Top 50 Colombia</p>', unsafe_allow_html=True)
    top_colombia = top_50_colombia()
    markdown_song(top_colombia)
with col2:
    st.markdown(f'<p class="artist-list-title">Top 50 Global</p>', unsafe_allow_html=True)
    top_global = top_50_global()
    markdown_song(top_global)
with col3:
    st.markdown(f'<p class="artist-list-title">Tu top 50</p>', unsafe_allow_html=True)
    top_tracks_user = user_top_tracks()
    markdown_song(top_tracks_user)

st.divider()
st.markdown('<div class="emoji-separator">...🧊🧊🧊🧊🧊...</div>', unsafe_allow_html=True)
st.markdown('<div></div>', unsafe_allow_html=True)
col1_1, col2_1 = st.columns(2)

with col1_1:
    st.markdown(f'<p class="artist-list-title">Tus canciones en común con los top 50 Colombia</p>', unsafe_allow_html=True)
    top_colombia = top_50_colombia()
    verify_tracks_in_common(top_colombia)
with col2_1:
    st.markdown(f'<p class="artist-list-title">Tus canciones en común con los top 50 Globales</p>', unsafe_allow_html=True)
    top_global = top_50_global()
    verify_tracks_in_common(top_global)