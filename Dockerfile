# Utiliser une image Python officielle comme base
FROM python:3.9
# Définir le répertoire de travail dans le conteneur
WORKDIR /app
# Copier les fichiers de votre projet dans le conteneur
COPY requirements.txt .
# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
# Copier le reste des fichiers du projet
COPY . .
# Exposer le port sur lequel l'application va fonctionner
EXPOSE 8000
# Définir la commande par défaut pour exécuter l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]