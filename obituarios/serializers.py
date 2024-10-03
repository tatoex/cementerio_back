from rest_framework import serializers
from .models import Obituario, Memoria, EtapasObituario

class ObituarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obituario
        fields= '__all__'

class MemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memoria
        fields= '__all__'

class EtapasObituarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapasObituario
        fields= '__all__'