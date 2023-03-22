import streamlit as st
import pandas as pd
from API import authorization
import numpy as np
import os

st.set_page_config(
    page_title="Data Analytics Spotify",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

ruta_css = os.path.join(os.getcwd(), "style.css")
with open(ruta_css) as f:
    css = '<style>{}</style>'.format(f.read())
    st.markdown(css, unsafe_allow_html=True)

login = st.container()
with login:
    welcome, container_inputs= st.columns(2)
    with container_inputs:
        st.title(":green[Spotify Data Analytics]")
        client_id = st.text_input('Client ID', placeholder ='Ingrese su client ID')
        client_secret = st.text_input("Client Secret",  placeholder ='Ingrese su client Secret',  type="password")
        re_direct_url =  st.text_input("Re-Direct URL", placeholder ='Re Direct URL')
        click_button = st.button("Analizar!", use_container_width = True)

    with welcome:
        st.markdown('''<div class="container-image-home">
                            <img class="image-home" src="https://play-lh.googleusercontent.com/P2VMEenhpIsubG2oWbvuLGrs0GyyzLiDosGTg8bi8htRXg9Uf0eUtHiUjC28p1jgHzo">
                       </div>''', unsafe_allow_html=True)

        if click_button:
            check_autorization, display_name = authorization(client_id, client_secret, re_direct_url)
            if check_autorization:
                st.markdown(f'<p class="message-home">Bienvenido {display_name}</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="message-home"> Error de los datos</p>', unsafe_allow_html=True)
                