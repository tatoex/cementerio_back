from rest_framework import serializers
from .models import Lote, Tumba, DisponibleTumba

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'
        read_only_fields = ('modified_by',)

class TumbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tumba
        fields = '__all__'
     

class DisponibleTumbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisponibleTumba
        fields = '__all__'
        