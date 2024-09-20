# MonProjet : Application de ECommerce

Ce projet est une application de commerce électronique développée avec Django et PostgreSQL. Il permet aux utilisateurs de naviguer à travers les produits, de les ajouter à leur panier et de passer des commandes. Le projet inclut des fonctionnalités telles que l'authentification des utilisateurs, la gestion des produits, le traitement des commandes, et la gestion des utilisateurs.


## Outils utilises : Python 3 , Django, PostgreSql, github
# installation de django
pip install django
# demarrer un projet django
python -m django startprojet nom du projet(mon_projet_ecommerce)
# a l'interieur du projet on va creer pluseurs applications

# pour creer une applicaion : python manager.py startapp apibackend

# relions notre projet a notre aplication apibackend(setting.py)

Framework utilisé pour les tests Untaires 
Framework de test : Les tests utilisent le framework intégré de Django, qui est basé sur unittest et est fourni par django.test.TestCase et rest_framework.test.APITestCase.





Après avoir clôné le repo :

# Recommandé : créez un environnement virtuel
$ virtualenv env
$ . env/bin/activate
python -m venv myenv

activer mon environnement virtuel


# Installez les dépendances
$ pip install -r requirements.txt

# Initialisez la Database create database (ses commandes permettent de crer mes tables en Bases de donnes)
python manage.py makemigrations
$ python manage.py migrate

# Lancez le serveur de dev
$ python manage.py runserver

API
Au cas où on voudrait utiliser cette app avec un frontend JS, une petite API REST a été implémentée à l'aide du Django REST Framework.

Les ressources utiles sont dispos sur le serveur Django :

Browsable API : http://localhost:8000/api/



## Liste des fonctionnalités principales du projet :

1 Inscription et Connexion

Création de compte
Connexion via email ou réseaux sociaux
Réinitialisation du mot de passe

2 Navigation et Recherche
Ajout des produits
Ajout des categories
Barre de recherche avec suggestions
Filtres et tri des produits par categories
Catégorisation des produits
Pages de produits avec descriptions détaillées

3 Gestion du Panier

Ajout et suppression d'articles
Mise à jour des quantités
Affichage du total et des frais de livraison

4 Processus de Commande

Choix des options de livraison
Sélection des méthodes de paiement (carte bancaire, PayPal, etc.)
Confirmation et récapitulatif de la commande

Ce projet n'est pas sous la licenc

relation entre les differentes tables de la BD
Un produit appartient à une seule catégorie (ForeignKey), mais une catégorie peut avoir plusieurs produits (related_name='produits').
Un avis est associé à un seul produit (ForeignKey), mais un produit peut avoir plusieurs avis (related_name='avis').
Un utilisateur a un seul panier (OneToOneField).
Un panier peut contenir plusieurs articles (ForeignKey), et chaque article est associé à un produit.
Un utilisateur peut passer plusieurs commandes (ForeignKey).
Une commande peut avoir plusieurs détails (ForeignKey), et chaque détail est associé à un produit.
Une commande a une seule transaction associée (OneToOneField).
Une commande a une seule expédition associée (OneToOneField).



### Résumé

Voici un résumé des étapes :

1. **Modèles Django** : Définir les modèles dans `models.py` pour représenter tes tables PostgreSQL.
2. **Sérializers** : Créer des sérializers dans `serializers.py` pour convertir les données des modèles en JSON et vice versa.
3. **Vues API** : Mettre en place des vues pour les API dans `views.py` en utilisant `viewsets` pour des opérations CRUD.
4. **Routage** : Configurer les routes dans `urls.py` pour exposer tes API.
5. **Paramètres** : Ajuster les paramètres de Django REST framework dans `settings.py`.



CI CD DU PROJET EXPLICATIONS:

image: python:3.9 : Détermine l'image Docker utilisée pour les jobs. Ici, nous utilisons une image Python 3.9.

variables : Déclare des variables d'environnement que vous pouvez utiliser dans vos jobs.

stages : Définit les différentes étapes du pipeline. Les étapes sont exécutées dans l'ordre où elles sont définies. Ici, nous avons deux étapes : test et deploy.

test : C'est un job qui se déroule pendant l'étape test.

services : Définit les services nécessaires, comme PostgreSQL dans ce cas.
before_script : Les commandes exécutées avant le script principal, comme l'installation des dépendances et la migration de la base de données.
script : Les commandes principales du job. Ici, nous exécutons les tests Django.
artifacts : Les fichiers ou répertoires à conserver après l'exécution du job. Ici, les résultats des tests sont stockés pour consultation ultérieure.
deploy : C'est un job qui se déroule pendant l'étape deploy.

script : Les commandes de déploiement à exécuter. Vous devez remplacer "Déploiement en cours" et ajouter les commandes spécifiques pour déployer votre application (comme la copie des fichiers sur le serveur, le redémarrage des services, etc.).
only : Spécifie que ce job doit être exécuté uniquement sur la branche master.

    Exécution du Pipeline
    Commit et Push : Commitez le fichier .gitlab-ci.yml et poussez-le sur votre dépôt GitLab :
    git add .gitlab-ci.yml
    git commit -m "Add CI/CD pipeline configuration"
    git push origin master




    Dockeiser mon application

    Le Dockerfile est un fichier de configuration qui décrit comment construire l'image Docker pour votre application Django.


FROM python:3.9 : Utilise une image Python 3.9 officielle comme base.
WORKDIR /app : Définit le répertoire de travail dans le conteneur.
COPY requirements.txt . : Copie le fichier requirements.txt dans le conteneur.
RUN pip install --no-cache-dir -r requirements.txt : Installe les dépendances Python
COPY . . : Copie le reste des fichiers de votre projet dans le conteneur.
EXPOSE 8000 : Expose le port 8000 pour que l'application soit accessible depuis l'extérieur.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"] : Définit la commande à exécuter lorsque le conteneur démarre. Remplacez myproject par le nom de votre projet.



version: '3.8' : Spécifie la version de Docker Compose utilisée.
services : Définit les services de votre application.
db : Service pour la base de données PostgreSQL
image: postgres:13 : Utilise l'image PostgreSQL 13.
environment : Définit les variables d'environnement nécessaires pour PostgreSQL
volumes : Crée un volume nommé postgres_data pour stocker les données PostgreSQL.
ports : Mappe le port 8000 du conteneur au port 8000 de l'hôte
epends_on : Assure que le service db démarre avant le service web.
volumes : Définit le volume persistant pour PostgreSQL.

Construire et lancer les conteneurs Docker :docker-compose up --build
docker-compose up : Démarre les services définis dans docker-compose.yml.
--build : Construit les images avant de lancer les conteneurs.


Appliquer les migrations de la base de données :Ouvrez un autre terminal et exécutez :
docker-compose exec web python manage.py migrate


Pour une application e-commerce typique, nous aurons besoin des endpoints suivants :

Utilisateurs (Users)

Créer un utilisateur
Obtenir un utilisateur
Mettre à jour un utilisateur
Supprimer un utilisateur

Produits (Products)

Créer un produit
Obtenir une liste de produits
Obtenir un produit
Mettre à jour un produit
Supprimer un produit

Commandes (Orders)

Créer une commande
Obtenir une liste de commandes
Obtenir une commande
Mettre à jour une commande
Supprimer une commande

pour verifier l'interface de swagger lancer le serveur a cette adresse : http://localhost:8000/swagger/
acceder a http://localhost:8000/redoc/ pour voir la documentation ReDoc

