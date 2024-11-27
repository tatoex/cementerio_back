from rest_framework import serializers
from .models import Articulo, Guia, ServicioInfo, SeccionArticulo

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = '__all__'

class ServicioInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioInfo
        fields = '__all__'

class SeccionArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeccionArticulo
        fields = '__all__'