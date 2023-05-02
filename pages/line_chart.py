import streamlit as st
from page_config import set_page_config, set_second_pages_title
from statistics_processes.making_line_chart import *
from API import *

set_page_config()
set_second_pages_title()

st.header('Grafica de popularidad de tus 15 canciones más escuchadas')
data = trigger_line_chart()
st.write("""
            La popularidad de una canción es un valor entre 0 y 100, siendo 100 la más popular, se calcula mediante un algoritmo y se basa, 
            en gran medida, en el número total de reproducciones que ha tenido la canción y en que tan recientes son.
            En general, las canciones que se están reproduciendo mucho en la actualidad tendrán una popularidad más alta que las canciones que se 
            reproducían mucho en el pasado. Las canciones duplicadas (por ejemplo, la misma canción de un sencillo y un álbum) se califican de forma 
            independiente.""")
with st.container():
    st.bar_chart(data.set_index('names').sort_values(by='popularity', ascending=False), height=600, width=25)
    
