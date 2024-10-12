from rest_framework import serializers
from .models import Deudo, Difunto
from tumba.serializers import TumbaSerializer

class DeudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deudo
        fields = [
            'id',
            'names',         # Campo del deudo
            'last_names',    # Campo del deudo
            'idNumber',      # Campo del deudo
            'phoneNumber',   # Campo del deudo
            'email',         # Campo del deudo
            'address',       # Campo del deudo
            'tipo',          # Campo del deudo
            'description',   # Campo del deudo
        ]

     
     
    
class DifuntoSerializer(serializers.ModelSerializer):
    tumba = TumbaSerializer(read_only=True)
    deudo = DeudoSerializer(read_only=True)
    class Meta:
        model = Difunto
        fields = [
            'id',
            'names',         # Campo del difunto
            'last_names',    # Campo del difunto
            'idNumber',      # Campo del difunto
            'requestNumber', # Campo del difunto
            'description',   # Campo del difunto
            'tumba',         # Objeto relacionado Tumba
            'deudo',         # Objeto relacionado Deudo
        ]
    