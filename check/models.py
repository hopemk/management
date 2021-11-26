from django.db import models

from employees.models import Employee
from items.models import Product

# Create your models here.
class CheckInOut(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #model = models.CharField(unique=True, max_length=50)
    #serial_number = models.CharField(unique=True, max_length=50)
    checkin_time = models.DateTimeField(auto_now_add=False)
    check_in = models.BooleanField(null=True, blank=True)
    checkout_time = models.DateTimeField(null=True, blank=True, auto_now_add=False)
    check_out = models.BooleanField(null=True, blank=True)
    

    def __str__(self):
        return self.employee.first_name

class ProductCheckInOut(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #model = models.CharField(unique=True, max_length=50)
    #serial_number = models.CharField(unique=True, max_length=50)
    checkin_time = models.DateTimeField(auto_now_add=False)
    check_in = models.BooleanField(null = True)
    checkout_time = models.DateTimeField(blank = True, null = True, auto_now_add=False)
    check_out = models.BooleanField(blank = True, null = True)
    

    def __str__(self):
        return self.employee.first_name
