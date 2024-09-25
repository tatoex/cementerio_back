from rest_framework import serializers
from .models import Deudo, Difunto

class DeudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deudo
        fields = '__all__'

class DifuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difunto
        fields = '__all__'