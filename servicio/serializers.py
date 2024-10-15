from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Servicio, Ceremonia
from tumba.serializers import TumbaSerializer
from difunto.serializers import DeudoSerializer, DifuntoSerializer

class CeremoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremonia
        fields = [
            'id',
            'names',         # Campo del servicio
            'date',          # Campo del servicio
            'description',   # Campo del servicio
            'is_paid',       # Campo del servicio
            'amount_paid',   # Campo del servicio
            'payment_date',  # Campo del servicio
        ]
        
class ServicioSerializer(serializers.ModelSerializer):
    deceased = DifuntoSerializer(read_only=True)
    ceremonia = CeremoniaSerializer(many=True,read_only=True)
    class Meta:
        model = Servicio
        fields = [
            'id',
            'startDate',     # Campo del servicio
            'endDate',       # Campo del servicio
            'description',   # Campo del servicio
            'deceased',      # Campo del servicio
            'numberTomb',    # Campo del servicio
            'ceremonia',     # Campo del servicio
        ]

class UserProfileSerializer(serializers.ModelSerializer): # Aquí se debe especificar many=True si es necesario
    class Meta:
        model = User
        fields = '__all__'  # O especifica los campos que necesites

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']  # Campos expuestos

