from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .models import Produtor
from .serializers import ProdutorSerializer
# Create your views here.


class ProdutorAPI(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer