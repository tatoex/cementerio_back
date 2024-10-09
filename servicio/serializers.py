from rest_framework import serializers
from .models import Servicio, Ceremonia
from tumba.serializers import TumbaSerializer
from difunto.serializers import DeudoSerializer, DifuntoSerializer

class ServicioSerializer(serializers.ModelSerializer):
    numberTomb = TumbaSerializer(read_only=True)
    deceased = DifuntoSerializer(read_only=True)
    deudo = DeudoSerializer(read_only=True)
    class Meta:
        model = Servicio
        fields = '__all__'

class CeremoniaSerializer(serializers.ModelSerializer):
    servicios = ServicioSerializer(read_only=True)
    class Meta:
        model = Ceremonia
        fields = '__all__'