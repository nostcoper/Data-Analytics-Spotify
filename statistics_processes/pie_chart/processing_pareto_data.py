import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def __get_cumulative_percentage(artists_dict: dict) -> tuple:
    df = pd.DataFrame(artists_dict.items(), columns=['artist', 'count']).sort_values(by=['count'], ascending=True)
    df['cumulative_percentage'] = (df['count'].cumsum() / df['count'].sum() * 100).round(2)
    print(df)
    return (df['artist'].tolist()[:5], df['cumulative_percentage'].tolist()[:5])

#Creates a figure and an axis and returns them
def __create_figure_and_axis() -> tuple:
    fig, ax = plt.subplots()
    return (fig, ax)

#Creates a pie chart and returns it
def __create_pie_chart(ax:plt.Axes,artists: list, percentages: list):
    ax.pie(percentages, labels=artists,explode=(0,0,0,0,0.1), autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')

def creates_pie(artist_dict: dict)-> plt.Figure:
    artists, percentages = __get_cumulative_percentage(artist_dict)
    fig, ax = __create_figure_and_axis()
    __create_pie_chart(ax, artists, percentages)
    return fig