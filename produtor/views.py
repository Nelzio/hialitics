from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .models import (
    Produtor,
    Ciclo,
    Contacto,
    Endereco,
    Pavilhao,
    ConsumoRacao,
    Mortalidade,
    Vacinacao,
    RequisicaoRacao,
    Racao,
    Peso
    )
from .serializers import (
    ProdutorSerializer,
    CicloSerializer,
    EnderecoSerializer,
    PavilhaoSerializer,
    ContactoSerializer,
    PesoSerializer,
    ConsumoRacaoSerializer,
    MortalidadeSerializer,
    RacaoSerializer,
    RequisicaoRacaoSerializer,
    VacinacaoSerializer,
    )
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


class MortalidadeAPI(viewsets.ModelViewSet):
    queryset = Mortalidade.objects.all()
    serializer_class = MortalidadeSerializer


class VacinacaoAPI(viewsets.ModelViewSet):
    queryset = Vacinacao.objects.all()
    serializer_class = VacinacaoSerializer


class RequisicaoRacaoAPI(viewsets.ModelViewSet):
    queryset = RequisicaoRacao.objects.all()
    serializer_class = RequisicaoRacaoSerializer


class RacaoAPI(viewsets.ModelViewSet):
    queryset = Racao.objects.all()
    serializer_class = RacaoSerializer


class PesoAPI(viewsets.ModelViewSet):
    queryset = Peso.objects.all()
    serializer_class = PesoSerializer


class ConsumoRacaoAPI(viewsets.ModelViewSet):
    queryset = ConsumoRacao.objects.all()
    serializer_class = ConsumoRacaoSerializer

    

