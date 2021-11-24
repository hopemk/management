from django.db import models
from employees.models import Employee
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(unique=True, max_length=50)
    #product_type = models.CharField(unique=True, max_length=50)
    serial_number = models.CharField(unique=True, max_length=50)
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #quantity_after_sale = models.IntegerField()
    date_issued = models.DateTimeField(auto_now_add=True)
    #price_per_item = models.FloatField(max_length=280)
    #title = models.CharField(max_length=280)

    def __str__(self):
        return self.model

