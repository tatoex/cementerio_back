from rest_framework import serializers
from .models import Obituario, Memoria, EtapasObituario
from difunto.serializers import DifuntoSerializer
from servicio.serializers import ServicioSerializer

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