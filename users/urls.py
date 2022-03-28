from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import UserView

app_name = 'user'

urlpatterns = [
    #path('products', product, name='product'),
    path('user', UserView.as_view(), name='user'),
    #path('product/<int:pk>/', ProductView.as_view(), name='product'),
    #path('sell/item/<int:pk>/', SellItemView.as_view(), name='sellitem'),
]