from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User
from posapp.models import Product, ProductSerializer
from django.db.models import Sum

from rest_framework import serializers


class SellItem(models.Model):
    #sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    items_sold = models.IntegerField()
    paid = models.FloatField(max_length=280)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name
    def get_object(val):
        try:
            return SellItem.objects.get(id=val)
        except:
            return False
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return self
class SellItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = SellItem
        fields = ['id', 'product', 'items_sold', 'paid', 'time']
class Sell(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #items_sold = models.IntegerField()
    total_paid = models.FloatField(default=0,max_length=280)
    time = models.DateTimeField(auto_now_add=True)
    sell_items = models.ManyToManyField(SellItem)
    #friends = models.ManyToManyField(Product)
    #quantity_after_sale = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return self
    def get_object(val):
        try:
            return Sell.objects.get(id=val)
        except:
            return False


    class Meta:
        ordering = ['time']

    
'''
    def __str__(self):
        return self.product.name
    
    @admin.display
    def sums(self):
        product_list = [product['product'] for product in Sell.objects.values('product').distinct()]
        num_of_items = Sell.objects.filter(product__in = set(product_list)).aggregate(Sum('items_sold'))
        return num_of_items['items_sold__sum']
        
    @admin.display
    def product_name(self):
        product_list = [product['product'] for product in Sell.objects.values('product').distinct()]
        return set(product_list)
    
    def save(self, *args, **kwargs):
        products = Sell.objects.values('product').distinct()
        
        print(Sell.objects.filter(product__in = set(products)).aggregate(Sum('items_sold')))
        #print(self.items_sold)
        #quantity = self.product.quantity_after_sale - self.items_sold
        #self.product.update(quantity_before_sale = quantity)
        #Pro.objects.filter(sell = self.product.name).update(quantity_after_sale = quantity)
        super().save(*args, **kwargs)
        '''
class SellSerializer(serializers.ModelSerializer):
    sell_items = SellItemSerializer(read_only=True, many=True)

    class Meta:
        model = Sell
        fields = ['id', 'sell_items', 'time']

class Sale(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #items_sold = models.IntegerField()
    #paid = models.FloatField(max_length=280)
    time = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product)

    



# Create your models here.
