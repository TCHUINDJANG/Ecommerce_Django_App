from django.db import models



class Customer(models.Model):
     name = models.CharField(max_length=200,null=True)
     email = models.CharField(max_length=200, null=True)
     phone_number = models.CharField(max_length=20, blank=True, null=True)

     def __str__(self):
             return self.name

class Category(models.Model):
        name = models.CharField(max_length=200)
        date_ajout = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['-date_ajout']

        def __str__(self):
             return self.name

class produits(models.Model):
    titre = models.CharField(max_length=100)
    prix = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie',on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_ajout = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()

    class Meta:
            ordering = ['-date_ajout'] 

      
    def __str__(self):
        return self.titre


class Commande(models.Model):
    customer_name = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.TextField()
    product = models.ForeignKey(produits, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Commande, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(produits, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
# Create your models here.
