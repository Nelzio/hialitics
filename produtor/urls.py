from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('produtor', views.ProdutorAPI)


urlpatterns = [
    path('api/', include(router.urls), name='url_produtor_api'),
]
