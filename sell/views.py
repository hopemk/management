from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sell
from django.db.models import Sum
from posapp.models import Product
# Create your views here.
def product(request):
    
    try:

        product_list = [product['product'] for product in Sell.objects.values('product').distinct()]
        print(list(set(product_list)))
        profits = []
        #num_of_items = [sums for sums in Sell.objects.filter(product__in = list(set(product_list))).aggregate(Sum('items_sold'))]
        for n in list(set(product_list)):
            profit =	{
                "product": "Ford",
                "items_sold": "Mustang",
                "profit": 1964
                }
            num_of_items = Sell.objects.filter(product = n).aggregate(Sum('items_sold'))
            p = Product.objects.get(id = n)
            print("price per item", p.price_per_item)
            print(num_of_items['items_sold__sum'])
            profit["product"] = p.name
            profit["items_sold"] = num_of_items['items_sold__sum']
            profit['sub_category'] = p.sub_category.name
            profit['category'] = p.sub_category.category.name
            profit['unit_price'] = p.price_per_item
            profit['procure_unit_price'] = p.procure_price_per_item
            profit["profit"] = num_of_items['items_sold__sum'] * (p.price_per_item - p.procure_price_per_item)
            print("running")
            profits.append(profit)
        
        
        sold = num_of_items
        #sold = num_of_items['items_sold__sum']
    except:
        profits = None

    context = { "profits" : profits}
    print(context)

    return render(request, 'profits_per_product.html', context)
