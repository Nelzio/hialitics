from django.db import models


class Endereco(models.Model):
    provincia = models.CharField(max_length=255, null=False)
    cidade = models.CharField(max_length=255, null=False)
    bairro = models.CharField(max_length=255, null=False)
    lat = models.CharField(max_length=255, null=True)
    longi = models.CharField(max_length=255, null=True)


class Contacto(models.Model):
    telefone = models.CharField(max_length=13, null=False)
    email = models.CharField(max_length=255, null=True)


class Produtor(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    email = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False)

