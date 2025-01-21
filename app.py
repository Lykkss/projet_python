import streamlit as st
import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
from fpdf import FPDF
import tempfile
from src.file_reader import file_reader

matplotlib.use("agg")

st.title("📊 Analyse comparative des données COVID")

st.markdown(
    """
    Cette application permet d'analyser et de comparer des données COVID :
    - Filtrer par pays, région, ou colonne spécifique.
    - Comparer les cas confirmés, décès, guérisons, cas actifs, etc., entre deux fichiers.
    - Générer des visualisations interactives pour les données croisées.
    """
)

# Fonction pour charger un fichier CSV
def load_file(option_label):
    upload_option = st.radio(
        f"📂 {option_label} - Sélectionnez la source du fichier",
        ("Charger un fichier depuis mon ordinateur", "Sélectionner un fichier local dans `data/`"),
        key=f"{option_label}_radio"
    )

    df = None
    if upload_option == "Charger un fichier depuis mon ordinateur":
        uploaded_file = st.file_uploader(f"Téléchargez un fichier CSV ({option_label})", type=["csv"], key=f"{option_label}_uploader")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.subheader(f"👀 Aperçu des données ({option_label})")
            st.dataframe(df)
    elif upload_option == "Sélectionner un fichier local dans `data/`":
        data_files = [f for f in os.listdir("data/") if f.endswith(".csv")]
        if data_files:
            selected_file = st.selectbox(
                f"📂 Choisissez un fichier ({option_label})",
                data_files,
                key=f"{option_label}_selectbox"
            )
            df = pd.read_csv(os.path.join("data", selected_file))
            st.subheader(f"👀 Aperçu des données ({option_label})")
            st.dataframe(df)
        else:
            st.warning(f"Aucun fichier CSV trouvé dans le répertoire `data/` pour {option_label}.")
    return df

# Fonction pour générer un PDF avec les graphiques
def generate_pdf_with_graphs(dataframe, graphs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Données filtrées avec graphiques", ln=True, align='C')

    # Ajout des colonnes
    pdf.set_font("Arial", size=10)
    for column in dataframe.columns:
        pdf.cell(40, 10, txt=str(column), border=1)
    pdf.ln()

    # Ajout des lignes
    for _, row in dataframe.iterrows():
        for value in row:
            pdf.cell(40, 10, txt=str(value), border=1)
        pdf.ln()

    # Ajout des graphiques
    for graph_path in graphs:
        pdf.add_page()
        pdf.image(graph_path, x=10, y=30, w=190)

    pdf_output = pdf.output(dest='S').encode('latin1')
    return BytesIO(pdf_output)

# Fonction pour sauvegarder un graphique temporairement
def save_graph_temp(fig):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(temp_file.name)
    return temp_file.name

# Chargement des deux fichiers
st.header("📂 Chargement des fichiers")
df1 = load_file("Fichier 1")
df2 = load_file("Fichier 2")

if df1 is not None and df2 is not None:
    st.subheader("🔎 Filtrer et comparer les données")

    # Filtrage par pays/région
    common_columns = list(set(df1.columns) & set(df2.columns))
    if "Country/Region" in common_columns:
        selected_countries = st.multiselect(
            "Pays ou Régions", 
            df1["Country/Region"].unique(), 
            key="filter_countries"
        )
        if selected_countries:
            df1 = df1[df1["Country/Region"].isin(selected_countries)]
            df2 = df2[df2["Country/Region"].isin(selected_countries)]

    if "WHO Region" in common_columns:
        selected_regions = st.multiselect(
            "Régions OMS", 
            df1["WHO Region"].unique(), 
            key="filter_regions"
        )
        if selected_regions:
            df1 = df1[df1["WHO Region"].isin(selected_regions)]
            df2 = df2[df2["WHO Region"].isin(selected_regions)]

    # Affichage des données filtrées
    st.write("### Données filtrées - Fichier 1")
    st.dataframe(df1)

    # Exportation des données filtrées avec graphiques
    graphs = []
    numeric_columns1 = df1.select_dtypes(include=["float64", "int64"]).columns
    numeric_columns2 = df2.select_dtypes(include=["float64", "int64"]).columns
    common_numeric_columns = set(numeric_columns1) & set(numeric_columns2)

    if common_numeric_columns:
        st.write("### Graphiques générés pour les colonnes numériques communes")
        for col in common_numeric_columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df1[col], label=f"{col} (Fichier 1)", linestyle="-")
            ax.plot(df2[col], label=f"{col} (Fichier 2)", linestyle="--")
            ax.set_title(f"Comparaison pour {col}")
            ax.set_xlabel("Index")
            ax.set_ylabel("Valeurs")
            ax.legend()
            ax.grid(alpha=0.3)
            st.pyplot(fig)
            
            # Sauvegarder le graphique
            graph_path = save_graph_temp(fig)
            graphs.append(graph_path)

    pdf_output = generate_pdf_with_graphs(df1, graphs)
    st.download_button(
        label="Télécharger les données filtrées avec graphiques (PDF)",
        data=pdf_output,
        file_name="données_filtrées_graphiques.pdf",
        mime="application/pdf"
    )
else:
    st.info("📂 Veuillez sélectionner ou télécharger deux fichiers CSV pour continuer.")

st.markdown("---")
st.markdown("💡 Développé par Nicolas, Yaël, Lisa")