import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_histogram(df, column):
    """
    Génère un histogramme pour une colonne spécifique.

    Args:
        df (pandas.DataFrame): Le dataframe contenant les données.
        column (str): La colonne à analyser.

    Returns:
        plt.Figure: L'objet matplotlib pour l'histogramme.
    """
    plt.figure(figsize=(8, 6))
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f"Distribution de {column}")
    plt.xlabel(column)
    plt.ylabel("Fréquence")
    plt.tight_layout()
    return plt.gcf() 

def plot_trend(df, date_column, value_column):
    """
    Génère une courbe de tendance dans le temps.

    Args:
        df (pandas.DataFrame): Le dataframe contenant les données.
        date_column (str): La colonne contenant les dates.
        value_column (str): La colonne à analyser.

    Returns:
        plt.Figure: L'objet matplotlib pour la courbe de tendance.
    """
    plt.figure(figsize=(10, 6))
    df[date_column] = pd.to_datetime(df[date_column])  # Conversion des dates
    df.sort_values(by=date_column, inplace=True)
    plt.plot(df[date_column], df[value_column], marker='o', linestyle='-', color='teal')
    plt.title(f"Tendance de {value_column} dans le temps")
    plt.xlabel("Date")
    plt.ylabel(value_column)
    plt.grid()
    plt.tight_layout()
    return plt.gcf()  # Retourne la figure actuelle

def plot_interactive_trend(df, date_column, value_column):
    """
    Génère une courbe interactive avec Plotly.

    Args:
        df (pandas.DataFrame): Le dataframe contenant les données.
        date_column (str): La colonne contenant les dates.
        value_column (str): La colonne à analyser.

    Returns:
        plotly.graph_objects.Figure: Graphique interactif Plotly.
    """
    df[date_column] = pd.to_datetime(df[date_column])
    fig = px.line(df, x=date_column, y=value_column, title=f"Tendance interactive : {value_column}")
    return fig
