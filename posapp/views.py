from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from .models import Product

# Create your views here.

class ProductView(APIView):
    model = Product

    def get(self, request, id):
        if id:
            product = Product.get_object(id)
            return Response({"data": product}, status=status.HTTP_404_NOT_FOUND)
        else:
            return  Response({"data": Product.objects.all()},
             status=status.HTTP_404_NOT_FOUND)
        return False
    def post(self, request):
        return False
    def put(self, request):
        return False
    def delete(self, request):
        return False
    
