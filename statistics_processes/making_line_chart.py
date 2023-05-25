from API import *
from data_recolection.data_line_chart import *
import pandas as pd
import streamlit as st

def trigger_line_chart():
    top = get_top_tracks_json(15)
    names, popularity = trigger_popularity_list(top)
    chart_data = pd.DataFrame({'names': names, 'popularity': popularity})
    return chart_data