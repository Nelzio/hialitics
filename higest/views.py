from django.shortcuts import render
from produtor.models import Produtor

# Create your views here.

def home_dash(request):
    return render(request, 'higest/index.html')


def add_integrado(request):
    data = {}
    data['produtors'] = Produtor.objects.all()
    return render(request, 'higest/addIntegrado.html', data)


def dtls_integrado(request):
    return render(request, 'higest/details.html')