import streamlit as st
from page_config import set_page_config, set_second_pages_title
from streamlit_extras.switch_page_button import switch_page
from data_recolection.data_common_tracks import *
from API import *

set_page_config()
set_second_pages_title()

common_top_tracks = 'Si mis canciones más escuchadas están en el top 50 de Colombia o global'
to_show_line_shart = 'Ver la grafica de popularidad de tus 15 canciones más escuchadas'
option = st.selectbox(
    '¿Qué te gustaría ver?',
    ('Escoja una opción', common_top_tracks, to_show_line_shart, 'Mobile phone'))

if st.button('Enviar'):
    if option == common_top_tracks:
        switch_page("common_top_tracks")
    elif option == to_show_line_shart:
        switch_page("line_chart")