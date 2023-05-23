import streamlit as st

def items_with_image(items_dict):
    markdown_list = []
    for item in items_dict:
        image = items_dict[item]['images'][0]['url']
        name = items_dict[item]['name']
        markdown = f'<div class="element-artist-list"><img class="image-artist-list" src="{image}"><h3>{name}</h3></div>'
        markdown_list.append(markdown)
    
    # Concatenar todos los elementos Markdown en un solo div "artist-list"
    artist_list_html = '<div class="artist-list">' + ''.join(markdown_list) + '</div>'
    st.markdown(artist_list_html, unsafe_allow_html=True)