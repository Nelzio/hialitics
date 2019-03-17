from rest_framework import serializers
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


class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Endereco
        fields = '__all__'


class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Contacto
        fields = '__all__'



class ProdutorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Produtor
        fields = '__all__'


class PavilhaoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pavilhao
        fields = '__all__'


class CicloSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ciclo
        fields = '__all__'


class ConsumoRacaoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ConsumoRacao
        fields = '__all__'
        


class MortalidadeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Mortalidade
        fields = '__all__'


class VacinacaoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Vacinacao
        fields = '__all__'


class RequisicaoRacaoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RequisicaoRacao
        fields = '__all__'


class RacaoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Racao
        fields = '__all__'


class PesoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Peso
        fields = '__all__'

    