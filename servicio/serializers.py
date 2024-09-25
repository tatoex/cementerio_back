from rest_framework import serializers
from .models import Servicio, Ceremonia

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class CeremoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremonia
        fields = '__all__'