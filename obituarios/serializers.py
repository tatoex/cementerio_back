from rest_framework import serializers
from .models import Obituario, Memoria, EtapasObituario
from difunto.serializers import DifuntoSerializer
from servicio.serializers import ServicioSerializer

class ObituarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Obituario
        fields= '__all__'

    def validate(self, data):
        extra_fields = set(self.initial_data.keys()) - set(self.fields.keys())
        if extra_fields:
            raise serializers.ValidationError(f"Campos no válidos: {extra_fields}")
        return data

class MemoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Memoria
        fields= '__all__'

class EtapasObituarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = EtapasObituario
        fields= '__all__'