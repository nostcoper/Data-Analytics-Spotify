import streamlit as st

def items_with_image(items_dict):
    for item in (items_dict):
        image = items_dict[item]['images'][0]['url']
        name = items_dict[item]['name']
        st.markdown(f'<div class= "artist-list">  <img class="image-artist-list" src="{image}"><h3>{name}</h3> </div>', unsafe_allow_html=True)