from rest_framework import serializers
from .models import Lote, Tumba, DisponibleTumba

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = [
            'id', 
            'blockName',        # Campo del Lote
            'typeblock',        # Campo del Lote
            'numbersblock',     # Campo del Lote
            'filas',            # Campo del Lote
            'columnas',         # Campo del Lote
            'limite',           # Campo del Lote
            'description',      # Campo del Lote
        ]
        read_only_fields = ('modified_by',)


class TumbaSerializer(serializers.ModelSerializer):
    nameLote = LoteSerializer(read_only=True)
    class Meta:
        model = Tumba
        fields = [
            'id', 
            'nicheNumber',   # Campo del Tumba
            'nicheType',     # Campo del Tumba
            'available',     # Campo del Tumba
            'description',   # Campo del Tumba
            'nameLote',      # Objeto relacionado lote
        ]
    

class DisponibleTumbaSerializer(serializers.ModelSerializer):
    numberTumba =TumbaSerializer(read_only=True)
    class Meta:
        model = DisponibleTumba
        fields = '__all__'
        