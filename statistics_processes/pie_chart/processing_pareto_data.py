import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# create a pandas dataframe from the artist dict
def create_dataframe_from_dict(top_artists_dict:dict)->pd.DataFrame:
    df = pd.DataFrame({'Artist': list(top_artists_dict.keys()), 
                       'Count': list(top_artists_dict.values())})
    
    df = df.sort_values(by='Count', ascending=False)
    return df

#gets the pandas dataframe and adds with the cumulative percentaje column
def add_cumulative_percentaje_column(df:pd.DataFrame)->pd.DataFrame:
    df['Cumulative Percentaje'] = df['Count'].cumsum() / df['Count'].sum() * 100
    return df

def create_bar_chart(df: pd.DataFrame, ax: plt.Axes) -> None:
    ax.bar(df['Artist'], df['Count'], color='C0')
    ax.set_ylabel('Count')
    ax.set_xlabel('Artists')

def create_line_chart(df: pd.DataFrame, ax: plt.Axes) -> None:
    ax2 = ax.twinx()
    ax2.plot(df['Artist'], df['Cumulative Percentaje'], color='C1', marker='D', ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter())
    ax2.set_ylabel('Cumulative Percentaje')

def set_xticklabels(ax: plt.Axes) -> None:
    plt.setp(ax.get_xticklabels(), rotation=90, ha='right')

def create_pareto_chart(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 8))
    create_bar_chart(df, ax)
    create_line_chart(df, ax)
    set_xticklabels(ax)
    plt.show()
