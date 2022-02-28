from django.db import models

from django.contrib.auth.models import User

from rest_framework import serializers

#from sell.models import Sell


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=50)
    quantity = models.IntegerField()
    #quantity_after_sale = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    price_per_item = models.FloatField(max_length=280)
    procure_price_per_item = models.FloatField(max_length=280)

    def __str__(self):
        return self.name

    def get_object(val):
        try:
            return Product.objects.get(name=val)
        except:
            return False


class ProductSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'sub_category', 'name','quantity', 'date_updated', 'price_per_item', 'procure_price_per_item']


