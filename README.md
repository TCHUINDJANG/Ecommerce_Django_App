# MonProjet : Api application ECommerce

Ce projet est une application de commerce électronique développée avec Django et PostgreSQL. Il permet aux utilisateurs de naviguer à travers les produits, de les ajouter à leur panier et de passer des commandes. Le projet inclut des fonctionnalités telles que l'authentification des utilisateurs, la gestion des produits, le traitement des commandes, et la gestion des utilisateurs.


## Outils utilises : Python 3 , Django, PostgreSql, github , gitLab(CI CD) , UniTest( Pour les tests unitaires) , React.js



Après avoir clôné le repo :

# Recommandé : créez un environnement virtuel
$ virtualenv env
$ . env/bin/activate


# Installez les dépendances
$ pip install -r requirements.txt

# Initialisez la Database
python manage.py makemigrations
$ python manage.py migrate

# Lancez le serveur de dev
$ python manage.py runserver

API
Au cas où on voudrait utiliser cette app avec un frontend JS, une petite API REST a été implémentée à l'aide du Django REST Framework.

Les ressources utiles sont dispos sur le serveur Django :

Browsable API : http://localhost:8000/api/



## Liste des fonctionnalités principales du projet :

1 Inscription et Connexion ( Utilisateurs)

Création de compte
Connexion via email ou réseaux sociaux
Réinitialisation du mot de passe
Mot de passe oublie

2 Navigation et Recherche
Ajout des produits
Ajout des categories
Barre de recherche avec suggestions
Filtres et tri des produits par categories
Catégorisation des produits
Pages de produits avec descriptions détaillées
Paggination pour la recherches des produits
Ajout des produits a sa liste de favoris
Prmotion des produits selon une date

3 Gestion du Panier

Ajout et suppression d'articles
Mise à jour des quantités
Affichage du total et des frais de livraison

4 Processus de Commande

Choix des options de livraison
Sélection des méthodes de paiement (carte bancaire, PayPal, etc.)
Confirmation et récapitulatif de la commande

5 Statistiques des ventes selon une periode defini par l'utilisateur

6 Configuration d'une pipeline CI CD avec Gitlab
7 Deploiement de l'applicatiion dans Docker afin d'obtenir une image
8 L'application a ete deploye sur un serveur (Pythonanywhere) afin de la rendre accessible partout dans le monde
