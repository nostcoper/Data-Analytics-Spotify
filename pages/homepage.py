import streamlit as st
import os
from API import *
from streamlit_extras.switch_page_button import switch_page
from data_recolection.recommendations.data_recommendations_collection import user_recommendations
from PIL import Image
from components import items_with_image_recomendations
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
            st.markdown('''
            <div class="container-image-home">
                <img class="image-menu" src="data:image/jpeg;base64,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">
            </div>
            ''', unsafe_allow_html=True)
            click_button_cloud= st.button("Analiza tus generos", use_container_width=True)
            if click_button_cloud:
                switch_page("word cloud")

    with side_right:
        items_with_image_recomendations(user_recommendations())