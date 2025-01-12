import streamlit as st
from src.file_reader import file_reader
from src.analyzer import analyze_csv
from src.visualizer import plot_histogram, plot_trend, plot_interactive_trend
import pandas as pd


st.title("Analyse des données COVID")

# Charger un fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

if uploaded_file:
    # Lire les données
    raw_data = file_reader(uploaded_file.name)
    if isinstance(raw_data, list):
        df = pd.DataFrame(raw_data[1:], columns=raw_data[0])

        # Afficher un aperçu des données
        st.subheader("Aperçu des données")
        st.dataframe(df.head())

        # Résumé des données
        st.subheader("Statistiques descriptives")
        stats = analyze_csv(uploaded_file.name)
        st.write(stats)

        # Sélection de la colonne pour les visualisations
        st.subheader("Visualisations")
        column = st.selectbox("Choisissez une colonne à visualiser", df.columns)

        if st.button("Afficher l'histogramme"):
            hist = plot_histogram(df, column)
            st.pyplot(hist)

        if st.button("Afficher la courbe de tendance"):
            trend = plot_trend(df, "Date", column)
            st.pyplot(trend)

        if st.button("Afficher un graphique interactif"):
            interactive_fig = plot_interactive_trend(df, "Date", column)
            st.plotly_chart(interactive_fig)
    else:
        st.error("Erreur dans le fichier chargé.")
else:
    st.info("Veuillez télécharger un fichier CSV pour commencer.")
