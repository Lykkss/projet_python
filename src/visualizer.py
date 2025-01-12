import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_histogram(df, column):
    """
    Generates a histogram for a specific column.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.
        column (str): The column to parse.

    Returns:
        plt.Figure: The matplotlib object for the histogram.
    """
    plt.figure(figsize=(10, 6))
    value_counts = df[column].value_counts()
    bars = plt.bar(value_counts.index, value_counts.values, color='skyblue')
    
    # Ajouter des annotations sur les barres
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')
    
    plt.title(f"Distribution de {column}", fontsize=16)
    plt.xlabel(column, fontsize=14)
    plt.ylabel("Fréquence", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return plt.gcf()


def plot_trend(df, date_column, value_column):
    """
    Generates a trend line over time.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.
        date_column (str): The column containing the dates.
        value_column (str): The column to analyze.

    Returns:
        plt.Figure: The matplotlib object for the trendline.
    """
    plt.figure(figsize=(12, 6))
    df[date_column] = pd.to_datetime(df[date_column])
    df.sort_values(by=date_column, inplace=True)

    plt.plot(df[date_column], df[value_column], marker='o', linestyle='-', color='teal', label=value_column)
    
    plt.title(f"Tendance de {value_column} dans le temps", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel(value_column, fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return plt.gcf()

def plot_interactive_trend(df, date_column, value_column):
    """
    Generates an interactive curve with Plotly.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.
        date_column (str): The column containing the dates.
        value_column (str): The column to analyze.

    Returns:
        plotly.graph_objects.Figure: Plotly interactive graph.
    """
    df[date_column] = pd.to_datetime(df[date_column])
    fig = px.line(
        df, 
        x=date_column, 
        y=value_column, 
        title=f"Tendance interactive : {value_column}",
        labels={date_column: "Date", value_column: "Valeur"},
        template="plotly_white",
        markers=True
    )
    fig.update_traces(line=dict(color='teal', width=3), marker=dict(size=8))
    fig.update_layout(
        title=dict(font=dict(size=20)),
        xaxis=dict(tickangle=45, title_font=dict(size=16), tickfont=dict(size=12)),
        yaxis=dict(title_font=dict(size=16), tickfont=dict(size=12)),
        legend=dict(font=dict(size=14))
    )
    return fig
