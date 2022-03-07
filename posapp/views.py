from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

import datetime

from .models import Product, ProductSerializer, Category, CategorySerializer, SubCategory, SubCategorySerializer

# Create your views here.

class CategoryView(APIView):
    model = Category

    def get(self, request, id = None):
        if id:
            category = Category.get_object(id)
            serializer = CategorySerializer(category)   
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many = True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):
        name = request.data['name']
        if not name:
            return  Response({"error": "Name not defined"},status=status.HTTP_404_NOT_FOUND)
        category = Category(
            name = name
        )
        category.save()
        return Response({"message": "saved"}, status=status.HTTP_201_CREATED )
    def put(self, request):
        category = Category.get_object(id)
        if not category:
            return  Response({"error": "Category not defined"},status=status.HTTP_404_NOT_FOUND)
        name = request.data['name']
        if not name:
            return  Response({"error": "Name not defined"},status=status.HTTP_404_NOT_FOUND)
        date_updated = datetime.now() 
        category.name = name
        category.date_updated = date_updated
        category.save()
        return Response({"message": "updated"}, status=status.HTTP_201_CREATED )
    def delete(self, request):
        data = request.data
        category = Category.get_object(data['category'])
        if category:
            category.delete()
        else:
            return Response({"error": "Category not available"}, status=status.HTTP_404_NOT_FOUND )
        return Response({"data": "deleted"}, status=status.HTTP_202_ACCEPTED )
class SubCategory(APIView):
    model = SubCategory
    def get(self, request, id):
        if id:
            sub_category = SubCategory.get_object(id)
            serializer = SubCategorySerializer(category)   
        else:
            sub_categories = SubCategory.objects.all()
            serializer = SubCategorySerializer(categories, many = True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        category = Category.get_object(data['category'])
        if not category:
            return  Response({"error": "Category not defined"},status=status.HTTP_404_NOT_FOUND)
        name = request.data['name']
        if not name:
            return  Response({"error": "Name not defined"},status=status.HTTP_404_NOT_FOUND)
        sub_category = SubCategory(
            name = name,
            category = category
        )
        sub_category.save()
        return Response({"message": "saved"}, status=status.HTTP_201_CREATED)
    def put(self, request):
        data = request.data
        category = Category.get_object(data['category'])
        if not category:
            return  Response({"error": "Category not defined"},status=status.HTTP_404_NOT_FOUND)
        name = request.data['name']
        if not name:
            return  Response({"error": "Name not defined"},status=status.HTTP_404_NOT_FOUND)
        date_updated = datetime.now()
        sub_category.category = category 
        sub_category.name = name
        sub_category.date_updated = date_updated
        sub_category.save()
        return Response({"message": "updated"}, status=status.HTTP_201_CREATED)
    def delete(self, request):
        data = request.data
        sub_category = SubCategory.get_object(data['sub_category'])
        if sub_category:
            sub_category.delete()
        else:
            return Response({"error": "SubCategory not available"}, status=status.HTTP_404_NOT_FOUND )
        return Response({"data": "deleted"}, status=status.HTTP_202_ACCEPTED )
class ProductView(APIView):
    model = Product

    def get(self, request, id = None):
        if id:
            product = Product.get_object(id)
            serializer = ProductSerializer(product)
            return Response({"data": serializer.data}, status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many = True)
            return  Response({"data": serializer.data},status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        data = request.data
        sub_category = SubCategory.get_object(data['sub_category'])
        if not sub_category:
            return  Response({"error": "SubCategory not Found"},status=status.HTTP_404_NOT_FOUND)
        else if not data['name']:
            return  Response({"error": "Name field is empty"},status=status.HTTP_404_NOT_FOUND)
        cat_name = data['name']
        product = Product(
            sub_category = sub_category,
            name = cat_name
        )
        product.save()
        return Response({"message": "save"}, status=status.HTTP_201_CREATED )
    def put(self, request):
        data = request.data
        product = Product.get_object(data['product'])
        if not product:
            return  Response({"error": "Product not Found"},status=status.HTTP_404_NOT_FOUND)
        sub_category = SubCategory.get_object(data['sub_category'])
        if not sub_category:
            return  Response({"error": "SubCategory not Found"},status=status.HTTP_404_NOT_FOUND)
        else if not data['name']:
            return  Response({"error": "Name field is empty"},status=status.HTTP_404_NOT_FOUND)
        cat_name = data['name']
        date_updated = datetime.now()

        product.sub_category = sub_category
        product.name = name
        product.date_updated = date_updated
        
        product.save()
        return Response({"message": "updated"}, status=status.HTTP_201_CREATED )
    def delete(self, request):
        data = request.data
        product = Product.get_object(data['product'])
        if product:
            product.delete()
        else:
            return Response({"error": "Product not available"}, status=status.HTTP_404_NOT_FOUND )
        return Response({"data": "deleted"}, status=status.HTTP_202_ACCEPTED )
    
