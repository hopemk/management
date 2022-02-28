from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ProductView

app_name = 'possapp'

urlpatterns = [
    #path('products', product, name='product'),
    path('product', ProductView.as_view(), name='product'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    #path('sell/item/<int:pk>/', SellItemView.as_view(), name='sellitem'),
]