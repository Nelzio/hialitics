from rest_framework import serializers
from .models import Produtor, Ciclo, Contacto, Endereco, Pavilhao


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