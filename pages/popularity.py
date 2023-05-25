import os
from API import *
import streamlit as st
from statistics_processes.line_chart.making_line_chart import *
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

st.markdown(f'<p class="message-popularity"> Gráfica de popularidad de tus canciones más escuchadas</p>', unsafe_allow_html=True)

try:
    data = trigger_line_chart()
except:
    st.error("No se ha podido conectar con Spotify, por favor inicia sesión nuevamente")
    time.sleep(5)
    switch_page("login")

st.write("""
            La popularidad de una canción es un valor entre 0 y 100, siendo 100 la más popular. En general, las canciones que se están reproduciendo mucho en la actualidad tendrán una popularidad más alta que las canciones que se 
            reproducían mucho en el pasado.""")
st.write("-----")
with st.container():
    table, graph = st.columns([6,15])
    with table:
        st.write(data)
    with graph:
        st.bar_chart(data.set_index('names').sort_values(by='popularity', ascending=False), height=400, width=25)