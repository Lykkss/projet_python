# Utiliser une image Python comme base
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /src

# Copier les fichiers nécessaires
COPY . /src

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port par défaut de Streamlit
EXPOSE 8501

# Lancer l'application Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false", "--server.address=0.0.0.0"]
