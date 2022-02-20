from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sell, SellSerializer, SellItem
from django.db.models import Sum
from posapp.models import Product

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

import json
from .utils import is_valid
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

class SellView(APIView):
    model = Sell

    def get(self, request):
        products = Sell.objects.all()
        serializer = SellSerializer(products, many = True)
        #print(products[0].product)
        #print(repr(serializer))
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        valid = is_valid(data)
        if valid:
            return Response({"data": valid}, status=status.HTTP_406_NOT_ACCEPTABLE)
        sell = Sell(
            #product = product,
            #items_sold = data['items_sold'],
            #paid = total_paid
        )
        sell = sell.save()
        '''
        if True:
            return Response({"data": sell}, status=status.HTTP_404_NOT_FOUND)
            '''
        #product = Product.objects.get(name = data['product'])
        total_paid = 0
        for item in data:
            product = Product.get_object(item['product'])
            items_sold = item['items_sold'] 
            paid = item['paid']
            sell_item = SellItem(
                #sell = sell,
                product = product,
                items_sold = items_sold,
                paid = paid
            )
            sell_item = sell_item.save()
            sell.sell_items.add(sell_item)
            sell.total_paid += paid
            sell.save()
        
        return Response({"message": "saved"}, status=status.HTTP_201_CREATED )

    def put(self, request):
        data = request.data
        #product = Product.objects.get(name = data['product'])
        valid = is_valid(data)

        if valid:
            return Response({"data": valid}, status=status.HTTP_406_NOT_ACCEPTABLE)
        product = Product.get_object(data['product'])
        if not product:
            return Response({"message": "product not available"}, status=status.HTTP_404_NOT_FOUND )
        
        
        sell = Sell(
            product = product,
            items_sold = data['items_sold'],
            paid = data['paid'],
        )
        sell.save()
        
        return Response({"message": "saved", "data":data}, status=status.HTTP_201_CREATED )
    
    def delete(self, request):
        data = request.data
        return Response({"message": "saved", "data":data}, status=status.HTTP_202_ACCEPTED )
    
    
