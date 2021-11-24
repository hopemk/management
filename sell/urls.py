from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import product

app_name = 'sell'

urlpatterns = [
    path('products', product, name='product'),
]