from rest_framework import serializers
from .models import Lote, Tumba

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
            'x',
            'y',
            'rotation','text_x',
            'text_y',
            'trans_r_x',
            'trans_r_y',
            'trans_t_x',
            'trans_t_y',
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
    

class LoteOcupacionSerializer(serializers.ModelSerializer):
    ocupadas = serializers.ReadOnlyField()
    disponibles = serializers.ReadOnlyField()

    class Meta:
        model = Lote
        fields = [
            'id',
            'blockName',
            'typeblock', 
            'numbersblock', 
            'ocupadas', 
            'disponibles',
            'limite', 
            'filas', 
            'columnas',
            'x',
            'y',
            'rotation','text_x',
            'text_y',
            'trans_r_x',
            'trans_r_y',
            'trans_t_x',
            'trans_t_y',
        ]