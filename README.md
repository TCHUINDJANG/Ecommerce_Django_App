# MonProjet : Ecommerce REST API
Swagger pour documenter les API Rest ( http://127.0.0.1:8000/swagger/)

Ecommerce-REST-API fournit des points de terminaison API pour vendre des produits physiques via le paiement Paypal/Stripe/Orange et MTN money. Conçu avec Python/Django et 100% gratuit à utiliser.


## Outils utilises : Python 3 , Django, PostgreSql, github , gitLab(CI CD) , UniTest( Pour les tests unitaires) 
                      

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

## Liste des fonctionnalités principales du projet :

L'administrateur peut créer/mettre à jour/supprimer une catégorie de produit
L'administrateur peut créer/mettre à jour/supprimer les détails du produit
Les utilisateurs authentifiés peuvent effectuer des requêtes POST sur la catégorie de produit et les détails du produit
Les utilisateurs non authentifiés ne peuvent effectuer des requêtes GET que sur la catégorie de produit et les détails du produit
Les utilisateurs peuvent s'inscrire pour être autorisés
Les utilisateurs autorisés peuvent effectuer des paiements et commander des produits

6 Configuration d'une pipeline CI CD avec Gitlab
7 Deploiement de l'applicatiion dans Docker afin d'obtenir une image et la partager
8 L'application a ete deploye sur un serveur (Pythonanywhere) afin de la rendre accessible partout dans le monde
