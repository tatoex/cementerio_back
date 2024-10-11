from rest_framework import serializers
from .models import Deudo, Difunto
from tumba.serializers import TumbaSerializer

class DeudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deudo
        fields = '__all__'

class DifuntoSerializer(serializers.ModelSerializer):
    # tumba = TumbaSerializer(read_only=True)
    # deudo = DeudoSerializer(read_only=True)
    class Meta:
        model = Difunto
        fields = '__all__'