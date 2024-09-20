from django.db import models



class User(models.Model): 
     name = models.CharField(max_length=200,null=True)
     email = models.EmailField(max_length=200, null=True)
     phone_number = models.CharField(max_length=20, blank=True, null=True)
     

     def __str__(self):
             return self.name

class Category(models.Model):
        name = models.CharField(max_length=200)
        date_ajout = models.DateTimeField(auto_now=True)
        description = models.TextField(max_length=500, null=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['-date_ajout']

        def __str__(self):
             return self.name

class produits(models.Model):
    titre = models.CharField(max_length=100)
    prix = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie',on_delete=models.CASCADE)
    image = models.CharField(max_length=100, null=True, blank=True )
    date_ajout = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()

    class Meta:
            ordering = ['-date_ajout'] 

      
    def __str__(self):
        return f"{self.titre} ({self.stock})"


class Commande(models.Model):
    customer_name = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    product = models.ForeignKey(produits, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.CharField(max_length=250, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)

    #permet de representer notre instance sous forme de chaine de caracterer
    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Commande, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(produits, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    



class Avis(models.Model):
    produit = models.ForeignKey(produits, on_delete=models.CASCADE, related_name='avis')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.utilisateur.username} - {self.produit.nom}'
    
class Panier(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    date_creation_commande = models.DateTimeField(blank=True,null=True)
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return f'Panier de {self.utilisateur.username}'


class ArticlesDuPanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, related_name='articles')
    produit = models.ForeignKey(produits, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.produit.nom} - {self.quantite}'
    

class DetailsCommandes(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='details')
    produit = models.ForeignKey(produits, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.produit.nom} - {self.quantite}'
    
    
class Transaction(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_transaction = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Transaction {self.id} - {self.commande.id}'
    

class Expedition(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    adresse_expedition = models.TextField()
    date_expedition = models.DateTimeField()
    statut = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Expédition {self.commande.id} - {self.statut}'
    
class Commentaire(models.Model):
        commentaire = models.OneToOneField(User, on_delete=models.CASCADE)
        adresse_expedition = models.TextField()
        date_commentaire = models.DateTimeField()
        statut = models.CharField(max_length=100)
    
        def __str__(self):
            return f'Expédition {self.commande.id} - {self.statut}'
# Create your models here.
