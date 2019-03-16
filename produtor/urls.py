from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('endereco', views.EnderecoAPI)
router.register('contacto', views.ContactoAPI)
router.register('produtor', views.ProdutorAPI)
router.register('pavilhao', views.PavilhaoAPI)
router.register('ciclo', views.CicloAPI)


urlpatterns = [
    path('api/', include(router.urls), name='url_produtor_api'),
]
