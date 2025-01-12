import streamlit as st
import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
from src.file_reader import file_reader
from src.visualizer import plot_trend, plot_interactive_trend

# Configurer Matplotlib pour le backend "agg"
matplotlib.use("agg")

# Titre de l'application
st.title("📊 Analyse des données COVID")

# Instructions pour l'utilisateur
st.markdown(
    """
    Cette application permet d'analyser et de croiser des données COVID :
    - Filtrer par pays, région, ou colonne spécifique.
    - Comparer les cas confirmés, décès, guérisons, cas actifs, etc.
    - Générer des visualisations interactives pour les données croisées.
    """
)

# Choix de la source du fichier
upload_option = st.radio(
    "📂 Sélectionnez la source du fichier",
    ("Charger un fichier depuis mon ordinateur", "Sélectionner un fichier local dans `data/`")
)

# Initialisation
df = None
file_path = None

# Charger un fichier depuis l'ordinateur
if upload_option == "Charger un fichier depuis mon ordinateur":
    uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])
    if uploaded_file:
        try:
            raw_data = file_reader(uploaded_file.name)
            if isinstance(raw_data, list) and len(raw_data) > 1:
                raw_data = [row for row in raw_data if any(row)]  # Supprimez les lignes vides
                column_count = len(raw_data[0])
                filtered_data = [row for row in raw_data if len(row) == column_count]
                df = pd.DataFrame(filtered_data[1:], columns=filtered_data[0])
                file_path = uploaded_file.name

                # Conversion des colonnes numériques
                for col in df.columns:
                    try:
                        df[col] = pd.to_numeric(df[col])
                    except ValueError:
                        continue  # Ignore les colonnes non numériques

                st.subheader("👀 Aperçu des données")
                st.dataframe(df)
            else:
                st.error("Le fichier est vide ou mal formaté. Veuillez vérifier vos données.")
        except Exception as e:
            st.error(f"Erreur lors du chargement du fichier : {e}")

# Charger un fichier depuis le répertoire `data/`
elif upload_option == "Sélectionner un fichier local dans `data/`":
    try:
        data_files = [f for f in os.listdir("data/") if f.endswith(".csv")]
        st.write(f"📂 Fichiers trouvés dans `data/` : {data_files}")
        if data_files:
            selected_file = st.selectbox("📂 Choisissez un fichier", data_files)
            try:
                raw_data = file_reader(selected_file)
                if isinstance(raw_data, list) and len(raw_data) > 1:
                    raw_data = [row for row in raw_data if any(row)]  # Supprimez les lignes vides
                    column_count = len(raw_data[0])
                    filtered_data = [row for row in raw_data if len(row) == column_count]
                    df = pd.DataFrame(filtered_data[1:], columns=filtered_data[0])
                    file_path = os.path.join("data", selected_file)

                    # Conversion des colonnes numériques
                    for col in df.columns:
                        try:
                            df[col] = pd.to_numeric(df[col])
                        except ValueError:
                            continue  # Ignore les colonnes non numériques

                    st.subheader("👀 Aperçu des données")
                    st.dataframe(df)
                else:
                    st.error("Le fichier est vide ou mal formaté. Veuillez vérifier vos données.")
            except Exception as e:
                st.error(f"Erreur lors du chargement du fichier : {e}")
        else:
            st.warning("Aucun fichier CSV trouvé dans le répertoire `data/`.")
    except Exception as e:
        st.error(f"Erreur lors de l'accès au répertoire `data/` : {e}")

# Si les données sont chargées
if df is not None:
    st.subheader("🔎 Filtrer et croiser les données")

    # Filtrer par pays ou région
    if "Country/Region" in df.columns:
        selected_countries = st.multiselect("Pays ou Régions", df["Country/Region"].unique())
        if selected_countries:
            df = df[df["Country/Region"].isin(selected_countries)]

    if "WHO Region" in df.columns:
        selected_regions = st.multiselect("Régions OMS", df["WHO Region"].unique())
        if selected_regions:
            df = df[df["WHO Region"].isin(selected_regions)]

    # Afficher les données filtrées
    st.write(f"### Données filtrées ({len(df)} lignes)")
    st.dataframe(df)

    # Visualisations
    st.subheader("📊 Comparaison des données filtrées")
    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns
    if len(numeric_columns) > 0:
        selected_columns = st.multiselect(
            "Choisissez des colonnes numériques à comparer",
            numeric_columns
        )
        if selected_columns:
            # Courbes comparatives
            st.write(f"### Courbes comparatives pour les colonnes sélectionnées : {', '.join(selected_columns)}")
            plt.figure(figsize=(10, 6))
            for col in selected_columns:
                plt.plot(df[col], label=col)
            plt.title("Comparaison des colonnes sélectionnées", fontsize=16)
            plt.xlabel("Index", fontsize=14)
            plt.ylabel("Valeurs", fontsize=14)
            plt.legend(fontsize=12)
            plt.grid(alpha=0.3)
            st.pyplot(plt.gcf())
            plt.close()
    else:
        st.warning("Aucune colonne numérique disponible pour les visualisations.")
else:
    st.info("📂 Veuillez sélectionner ou télécharger un fichier CSV pour continuer.")

# Footer
st.markdown("---")
st.markdown(
    "💡 Développé par Lina, Yaël, Lisa"
)
