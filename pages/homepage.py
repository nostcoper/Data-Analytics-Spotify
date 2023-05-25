import streamlit as st
import os
from API import *
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
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

ruta_css = os.path.join(os.getcwd(), "style_homepage.css")
with open(ruta_css) as f:
    css = '<style>{}</style>'.format(f.read())
    st.markdown(css, unsafe_allow_html=True)

margins_css = """
    <style>
        .main > div {
            padding-left: 0rem;
            padding-right: 0rem;
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

st.markdown(f'<p class="message-menu"> Curiosidades de tu música </p>', unsafe_allow_html=True)
menu = st.container()

side_left, side_right = st.columns([15,15])

with menu:
    with side_left:
        A, B = st.columns([15,15])
        with A:
            st.markdown("""
            <style>
            .custom-container {
                background-color: #f1f1f1; /* Cambia el color de fondo aquí */
                padding: 20px;
            }
            </style>
            """, unsafe_allow_html=True)
            container = st.container()
            st.markdown('''
            <div class="container-image-home">
                <img class="image-menu" src="https://charts-images.scdn.co/assets/locale_en/regional/daily/region_global_default.jpg">
            </div>
            ''', unsafe_allow_html=True)

            click_button_common_tracks = st.button("¿Escuchas los Top?", use_container_width=True)
            st.write("Averigua si tu top 50 tiene algo en común con el de Colombia y global")
            if click_button_common_tracks:
                switch_page("common tracks")
        
        with B:
            st.markdown("""
            <style>
            .custom-container {
                background-color: #f1f1f1; /* Cambia el color de fondo aquí */
                padding: 20px;
            }
            </style>
            """, unsafe_allow_html=True)
            container = st.container()
            st.markdown('''
            <div class="container-image-home">
                <img class="image-menu" src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcS4-KOY5_57P7o44GNt9HJrmENtN4E8LqPkujvx07KI40FBVQNl">
            </div>
            ''', unsafe_allow_html=True)
            click_button_popularity= st.button("Grafica de popularidad ", use_container_width=True)
            if click_button_popularity:
                switch_page("popularity")

            st.write("Ver la gráfica de popularidad de tu 15 canciones más escuchadas")

        C ,D = st.columns([15,15])
        with C:

            image = Image.open('grafico-de-torta.png')
            st.image(image)
            click_button_artits_graph = st.button("Aristas más escuchados", use_container_width=True)
            if click_button_artits_graph:
                switch_page("top artist")

        with D:
            pass  
