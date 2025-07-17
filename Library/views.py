from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class BookView(ModelViewSet):

    queryset=Book.objects.all()
    serializer_class=Book_Serializer


class LaptopView(generics.ListCreateAPIView):

    queryset=Laptops.objects.all()
    serializer_class=Laptops_Serializer

class LaptopViewByID(generics.RetrieveUpdateDestroyAPIView):

    queryset=Laptops.objects.all()
    serializer_class=Laptops_Serializer