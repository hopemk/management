from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    est = models.DateTimeField(blank = True, auto_now_add=False)
    location = models.CharField(max_length=100, blank=True, null=True)