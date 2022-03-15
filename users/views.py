from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

# Create your views here.
class UserView(APIView):
    model = Profile

    def get(self, request, pk = None):
        if pk:
            profile = Profile.get_object(pk)
            serializer = CompanySerializer(company)
        else:
            companies = Company.objects.all()
            serializer = CompanySerializer(Company, many = True)
        #print(products[0].product)
        #print(repr(serializer))
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        TP_400_BAD_REQUEST)
        user_serializer = UserSerializer(
            email = data['email'],
            password= data['password']
            first_name = data['firstName'],
            last_name = data['lastName']
        )
        if user_serializer.is_valid():
            user = user_serializer.save()
            if not user:
                return Response(user_proserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        profile_serializer = ProfileSerializer(
            user = user,
            bio = data['bio'],
            nationality = data['nationality'],

        )
        if profile_serializer.is_valid():
            profile = profile_serializer.save()
            if not profile:
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

        '''
        name = data['name']
        if not name:
            return Response({"message": "Name not defined"}, status=status.HTTP_404_NOT_FOUND )
        est = data['est']
        if not est:
            return Response({"message": "Esr not defined"}, status=status.HTTP_404_NOT_FOUND )
        location = data['location']
        if not location:
            return Response({"message": "Location not Defined"}, status=status.HTTP_404_NOT_FOUND )
        company = Company(
            name = name;
            est = est,
            location = location
        )
        company.save()
        '''
        return Response({"message": "saved", "data":data}, status=status.HTTP_201_CREATED )
    def put(self, request):
        data = request.data
        company = Company.get_object(data['company_id'])
        if not company:
            return Response({"message": "Name not defined"}, status=status.HTTP_404_NOT_FOUND )
        name = data['name']
        if not name:
            return Response({"message": "Name not defined"}, status=status.HTTP_404_NOT_FOUND )
        est = data['est']
        if not est:
            return Response({"message": "Esr not defined"}, status=status.HTTP_404_NOT_FOUND )
        location = data['location']
        if not location:
            return Response({"message": "Location not Defined"}, status=status.HTTP_404_NOT_FOUND )
        company.name = name
        company.est = est
        company.location = location
        company.save()
        return Response({"message": "saved"}, status=status.HTTP_201_CREATED )