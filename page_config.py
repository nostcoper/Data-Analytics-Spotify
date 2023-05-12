import streamlit as st
import os

def set_page_config():
    st.set_page_config(
        page_title = "Data Analytics Spotify",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def remove_margin_pages():
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