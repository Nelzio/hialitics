from django.db import models


class Endereco(models.Model):
    provincia = models.CharField(max_length=255, null=False)
    cidade = models.CharField(max_length=255, null=False)
    bairro = models.CharField(max_length=255, null=False)
    lat = models.CharField(max_length=255, null=True, blank=True)
    longi = models.CharField(max_length=255, null=True, blank=True)


class Contacto(models.Model):
    telefone = models.CharField(max_length=13, null=False)
    email = models.CharField(max_length=255, null=True)


class Produtor(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False)


class Pavilhao(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    codigo_pav = models.CharField(max_length=255, null=True)
    capacidade = models.PositiveIntegerField()


class Ciclo(models.Model):
    pavilhao = models.ForeignKey(Pavilhao, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField()
    quantidade = models.PositiveIntegerField()


class Racao(models.Model):
    tipo = models.CharField(max_length=255, null=False)

class RequisicaoRacao(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    racao = models.ForeignKey(Racao, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)


class ConsumoRacao(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    quantidade = models.PositiveIntegerField()


class Mortalidade(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    causa = models.CharField(max_length=255, null=False)
    quantidade = models.PositiveIntegerField()


class Peso(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    quantidade = models.PositiveIntegerField()


class Vacinacao(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=255, null=False)
    dias = models.PositiveIntegerField()





