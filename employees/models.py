from django.db import models

# Create your models here.
class Employee(models.Model):
    #sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    first_name = models.CharField(unique=True, max_length=50)
    last_name = models.CharField(unique=True, max_length=50)
    #quantity = models.IntegerField()
    #supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #quantity_after_sale = models.IntegerField()
    date_of_birth = models.DateTimeField(auto_now_add=False)
    #price_per_item = models.FloatField(max_length=280)
    title = models.CharField(max_length=280)
    is_employee = models.BooleanField(null = True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

