from django.contrib import admin
from .models import Category, produits



class AdminCategory(admin.ModelAdmin):

    list_display = ('name','date_ajout')

class AdminProduct(admin.ModelAdmin):

    list_display = ('titre','prix', 'category','date_ajout')
# Register your models here.
admin.site.register(produits , AdminProduct)
admin.site.register(Category , AdminCategory)
