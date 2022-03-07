from django.db import models

# Create your models here.
class Quantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time_created= models.DateTimeField(auto_now_add=True)