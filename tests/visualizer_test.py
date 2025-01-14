import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from visualizer import plot_histogram, plot_trend, plot_interactive_trend


def get_sample_dataframe():
    """
    Retourne un DataFrame d'exemple pour les tests.
    """
    data = {
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
        "Confirmed": [100, 150, 200, 250],
        "Deaths": [10, 15, 20, 25],
        "Recovered": [50, 80, 120, 150]
    }
    return pd.DataFrame(data)

def test_plot_histogram():
    """
    Teste la fonction plot_histogram pour s'assurer qu'un objet matplotlib Figure est retourné.
    """
    df = get_sample_dataframe()
    plt_obj = plot_histogram(df, "Confirmed")
    assert isinstance(plt_obj, plt.Figure), "plot_histogram n'a pas retourné un objet matplotlib Figure."
    print("✅ test_plot_histogram passé avec succès.")

def test_plot_trend():
    """
    Teste la fonction plot_trend pour s'assurer qu'un objet matplotlib Figure est retourné.
    """
    df = get_sample_dataframe()
    plt_obj = plot_trend(df, "Date", "Deaths")
    assert isinstance(plt_obj, plt.Figure), "plot_trend n'a pas retourné un objet matplotlib Figure."
    print("✅ test_plot_trend passé avec succès.")

def test_plot_interactive_trend():
    """
    Teste la fonction plot_interactive_trend pour s'assurer qu'un objet Plotly Figure est retourné.
    """
    df = get_sample_dataframe()
    plotly_fig = plot_interactive_trend(df, "Date", "Recovered")
    assert isinstance(plotly_fig, go.Figure), "plot_interactive_trend n'a pas retourné un objet Plotly Figure."
    print("✅ test_plot_interactive_trend passé avec succès.")

if __name__ == "__main__":
 
    test_plot_histogram()
    test_plot_trend()
    test_plot_interactive_trend()
