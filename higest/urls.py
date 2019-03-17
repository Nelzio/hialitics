from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home_dash, name='url_dash'),
    path('add-integrado', views.add_integrado, name='url_add_int'),
    path('details', views.dtls_integrado, name='url_dtls'),
]
