from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('endereco', views.EnderecoAPI)
router.register('contacto', views.ContactoAPI)
router.register('produtor', views.ProdutorAPI)
router.register('pavilhao', views.PavilhaoAPI)
router.register('ciclo', views.CicloAPI)


router.register('vacinacao', views.VacinacaoAPI)
router.register('req-medicamento', views.RequisicaoRacaoAPI)
router.register('consumo-racao', views.ConsumoRacaoAPI)
router.register('mortalidade', views.MortalidadeAPI)
router.register('peso', views.PesoAPI),

urlpatterns = [
    path('api/', include(router.urls), name='url_produtor_api'),
]
