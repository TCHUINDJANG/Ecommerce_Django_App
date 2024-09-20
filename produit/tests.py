from django.test import TestCase , Client
from .models import produits , Category
from django.utils import timezone
from django.urls import reverse
import json
from rest_framework import status

# Create your tests here.
#commande django pour lancer les test :python manage.py test
#la methode setUp va se lancer chaque fois qu'un test va debuter
#elle est execute avant chaque methode de test

class TestCaseProduits(TestCase):

# créons des objets nécessaires pour les tests.
#ceci permet d'eviter de creer les meme donnes dans chaque test individuel
    def setUp(self):
        self.category = Category.objects.create(nom='Electronique')
        self.produit = produits.objects.create_produit(
            titre = 'Ordinateur portable',
            prix = 1000,
            description = 'Un ordinateur portable de haute performance',
            category = self.category,
            image = 'chemin/vers/image.jpg',
            date_ajout = timezone.now(),
            stock = 10 
        )

        self.produit = produits.objects.create(
            produit = self.produit,
            titre = self.produit.titre
        )





    def test_list_products(self):

        """Test de la récupération de tous les produits"""
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertEqual(len(response.data) , 1)



    def test_get_product_by_id(self):
        """Test de la récupération d'un produit par ID"""
        response = self.client.get(reverse('product-detail' , args=[self.produit.id]))
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertEqual(response.data['titre'] , 'Ordinateur portable')
        self.assertEqual(response.data['description'] , 'Un ordinateur portable de haute performance')






    def test_produit(self):
        self.assertEqual(self.produit.titre , self.produit)

    def test_profil_titre(self):
        self.assertEqual(self.produit.produit , self.produit)



    def test_creation_produit(self):
            
            """Test de la création d'un nouveau produit"""

            data = {
                'titre':'Nouveau produit',
                'description':'Tres bon pour la sante',
                'stock':50
            }

            response = self.client.post(reverse('product-list') , data , format='json')
            self.assertEquals(produits.titre , 'Ordinateur portable')
            self.assertEquals(produits.prix , 1000)
            self.assertEquals(produits.description,'Un ordinateur portable de haute performance')
            self.assertEquals(produits.category, self.category)
            self.assertEquals(produits.image , 'chemin/vers/image.jpg')
            self.assertEquals(produits.stock , 10)
            self.assertEqual(produits.objects.count() , 2)



    def test_update_product(self):
         """Test de la mise à jour d'un produit existant"""

         data = {
             'titre' : 'Produit mis a jour',
             'prix': 50,
             'description':'Nouvelle desription',
             'stock':75
         }

         response = self.client.put(reverse('product-detail', args=[self.product.id]), data, format='json')

         self.assertEqual(response.status_code , status.HTTP_200_OK)
         self.produit.refresh_from_db()
         self.assertEqual(self.produit.prix , 50)
         self.assertEqual(self.produit.stock , 75)


    def test_delete_product(self):
        """Test de la suppression d'un produit"""

        response = self.client.delete(reverse('product-detail', args=[self.product.id]))
        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
        self.assertEqual(produits.objects.count() , 0)


    def test_filter_products_by_price(self):
         """Test de la récupération de produits avec un prix supérieur"""
         response = self.client.get(reverse('product-list') + '?price__gt=15')
         
         self.assertEqual(response.status_code , status.HTTP_200_OK)
         self.assertGreater(len(response.data) , 0)
            

    def test_search_producr(self):
        """Test de la recherche de produits par nom"""

        response = self.client.get(reverse('product-list') + '?search=Test')

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertEqual(len(response) , 1)


    def test_get_products_in_stocks(self):
         """Test de la récupération de produits en stock"""

         response = self.client.get(reverse('product-list') + '?stock__gt=0')

         self.assertEqual(response.status_code , status.HTTP_200_OK)
         self.assertGreater(len(response.data) , 0)



# Vérifiez la méthode __str__ pour s'assurer qu'elle retourne le bon titre
    def test_productt_str_method(self):
        
        self.assertEqual(str(self.produit),'Ordinateur portable')



#  Teste l'ordre de tri des objets Produits en fonction de date_ajout.je vais enregistrer deux produits
    def test_produit_ordering(self):

      produit1 = produits.objects.create(
          titre = 'Ancien produit',
          prix = 100.00, 
          description ='Produit plus ancien.',
          category= self.category,
          image='chemin/vers/ancien_image.jpg',
          date_ajout=timezone.now() - timezone.timedelta(days=1),
          stock=5
      )

      produit2 = produits.objects.create(
            titre='Tablet',
            prix=199.99,
            description='Une tablette avec un grand écran.',
            category=self.category,
            image='http://example.com/tablet.jpg',
            stock=20
        )

      produits = list(produits.objects.all())
      self.assertEqual(produits[0], produit1)
      self.assertEqual(produits[1], produit2)


    def test_valid_prix(self):
        # Testez si le prix est bien stocké en tant que float
        produit = self.produit
        self.assertIsInstance(produit.prix , float)


    def test_stock_never_negative(self):
        # Testez que le stock ne peut jamais être négatif
        with self.assertRaises(ValueError):
            produits.objects.create(
                titre='Negative Stock Item',
                prix=100.00,
                description='Un article avec stock négatif.',
                category=self.category,
                image='http://example.com/negative_stock.jpg',
                stock=-10
            )
class Produits_get_list_product_API(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('http://127.0.0.1/api/produit/')

    def test_get_produits(self):
        # Creons des objets produit pour le test
        produit1 = produits.objects.create(ProduitId=1, nom="Produit 1", prix=10.0)
        produit2 = produits.objects.create(ProduitId=2, nom="Produit 2", prix=20.0)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 2)  # Assurez-vous qu'il y a deux produits dans la réponse
        self.assertEqual(response_data[0]['nom'], produit1.nom)
        self.assertEqual(response_data[1]['nom'], produit2.nom)


    def test_post_product(self):
        produit_data = {
            'titre' : 'medicaments',
            'description': 'efferviscents',
            'category' :'efferalgan'
        }

        response = self.client.post(self.url , data=json.dumps(produit_data), content_type='application/json')
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        self.assertEqual(response.content.decode() , "Ajout du produit avec success")

        # Vérifiez que le produit a bien été ajouté
        produit_obj = produits.objects.get(ProduitId=3)
        self.assertEqual(produit_obj.nom, 'Produit 3')


    def test_put_produit(self):
        produit = produit.objects.create(ProduitId=4, nom="Produit 4", prix=40.0)
        update_data = {
            'ProduitId': 4,
            'nom': 'Produit 4 Updated',
            'prix': 45.0
        }

        response = self.client.put(self.url, data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode(), "Update Successful")

        # Vérifiez que le produit a bien été mis à jour
        produit_obj = produit.objects.get(ProduitId=4)
        self.assertEqual(produit_obj.nom, 'Produit 4 Updated')
        self.assertEqual(produit_obj.prix, 45.0)


    def test_delete_produit(self):
        produit = produit.objects.create(ProduitId=5, nom="Produit 5", prix=50.0)
        response = self.client.delsete(f'{self.url}?id=5')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.json()['message'], 'produit was deleted successfully!')

        # Vérifiez que le produit a bien été supprimé
        with self.assertRaises(produit.DoesNotExist):
            produit.objects.get(ProduitId=5)
    