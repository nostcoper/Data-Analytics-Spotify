import streamlit as st
import pandas as pd
from API import user



st.set_page_config(
    page_title="Data Analytics Spotify",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Spotify Data Analytics")
st.write(f"Bienvenido, {user['display_name']}!")