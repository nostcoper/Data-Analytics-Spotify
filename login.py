import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from API import authorization
from page_config import set_page_config, remove_margin_pages
import numpy as np
import os

set_page_config()

# Using "with" notation
with st.sidebar:
    pass

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
            try:
                os.remove(".cache")
            except FileNotFoundError:
                pass
            #check_autorization, display_name = authorization('41496547b72b4bb293055ca32f73069c', 'c23c8e7a2a39428889be937501708a5e', 'http://localhost:8080')
            check_autorization, display_name = authorization('f05c926d1d644bc8b3662d47f1849af2', '30392342f26f4e688435ffbc80639ee1', 'http://localhost:8080')
            #check_autorization, display_name = authorization(client_id, client_secret, re_direct_url)
            
            if check_autorization:
                switch_page("homepage")
            else:
                st.markdown('<p class="message-home"> Error de los datos</p>', unsafe_allow_html=True)
                