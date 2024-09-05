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





Après avoir clôné le repo :

# Recommandé : créez un environnement virtuel
$ virtualenv env
$ . env/bin/activate


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


