import pandas as pd
import altair as alt


def __get_cumulative_percentage(artists_dict: dict) -> pd.DataFrame:
    df = pd.DataFrame(artists_dict.items(), columns=['artist', 'count']).sort_values(by=['count'], ascending=False)
    df['percentage'] = (df['count']/ df['count'].sum() * 100).round(2)
    df.drop('count', axis=1, inplace=True)
    return df

def __create_pie_chart(df: pd.DataFrame) -> alt.Chart:
    chart = alt.Chart(df).mark_arc().encode(
        theta='percentage',
        color='artist',
        tooltip=['artist', 'percentage']
    )
    return chart


def creates_pie(artist_dict: dict)-> alt.Chart:
    df = __get_cumulative_percentage(artist_dict)
    chart = __create_pie_chart(df)
    return chart
    