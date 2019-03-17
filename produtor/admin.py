from django.contrib import admin
from .models import Ciclo, Contacto, Endereco, Pavilhao, Produtor

# Register your models here.
admin.site.register(Ciclo)
admin.site.register(Contacto)
admin.site.register(Endereco)
admin.site.register(Pavilhao)
admin.site.register(Produtor)