import streamlit as st
import os
from API import *
from streamlit_extras.switch_page_button import switch_page
import time

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
            padding-left: 3rem;
            padding-right: 3rem;
            padding-top: 0rem;
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)
try:
    display_name = sp.current_user()['display_name']
except:
    st.error("No se ha podido conectar con Spotify, por favor inicia sesión nuevamente")
    time.sleep(5)
    switch_page("login")

st.markdown(f'<p class="message-home"> Bienvenido {display_name}</p>', unsafe_allow_html=True)

side_left, separate ,side_right = st.columns([15,1,15])

with side_left:
    A, separate ,B = st.columns([15,1,15])
    with A:
        st.markdown('''<div class="container-image-home">
            <img class="image-common" src="https://charts-images.scdn.co/assets/locale_en/regional/daily/region_global_default.jpg">
        </div>''', unsafe_allow_html=True)
        st.markdown(f'<p class="/p>', unsafe_allow_html=True)
        click_button = st.button("Analizar!", use_container_width = True)

        if click_button:
            switch_page("common tracks")
    
    with B:
       pass


    C, separate ,D = st.columns([15,1,15])
    with A:
        st.write("C")
    with B:
        st.write("D")   
