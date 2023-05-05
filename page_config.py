import streamlit as st
from API import sp
import os

def set_page_config():
    st.set_page_config(
        page_title="Data Analytics Spotify",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def set_second_pages_title():
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