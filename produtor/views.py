from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .models import Produtor, Pavilhao, Ciclo, Endereco, Contacto
from .serializers import ProdutorSerializer, CicloSerializer, EnderecoSerializer, PavilhaoSerializer, ContactoSerializer
# Create your views here.


class EnderecoAPI(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ContactoAPI(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer


class ProdutorAPI(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer


class PavilhaoAPI(viewsets.ModelViewSet):
    queryset = Pavilhao.objects.all()
    serializer_class = PavilhaoSerializer


class CicloAPI(viewsets.ModelViewSet):
    queryset = Ciclo.objects.all()
    serializer_class = CicloSerializer