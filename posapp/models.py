from django.db import models

from django.contrib.auth.models import User

#from sell.models import Sell


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

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




