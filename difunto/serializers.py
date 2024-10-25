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
    tumba_ob = TumbaSerializer(source='tumba', read_only=True)
    deudo_ob = DeudoSerializer(source='deudo', read_only=True)

    class Meta:
        model = Difunto
        fields = [
            'id', 
            'names', 
            'last_names', 
            'idNumber', 
            'requestNumber', 
            'description', 
            'tumba',       # ID de tumba
            'tumba_ob',    # Objeto tumba completo
            'deudo',       # ID de deudo
            'deudo_ob'     # Objeto deudo completo
        ]
        extra_kwargs = {
            'tumba': {'required': False},
            'deudo': {'required': True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request and request.method != 'GET':
            representation.pop('tumba_ob', None)
            representation.pop('deudo_ob', None)
        return representation