from rest_framework import serializers
from .models import Produtor


class ProdutorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Produtor
        fields = '__all__'