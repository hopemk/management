from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import product, SellView, SellItemView

app_name = 'sell'

urlpatterns = [
    #path('products', product, name='product'),
    path('sell', SellView.as_view(), name='sell'),
    path('sell/<int:pk>/', SellView.as_view(), name='sell'),
    path('sell/item/<int:pk>/', SellItemView.as_view(), name='sellitem'),
]