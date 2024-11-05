from django.contrib.auth.models import User, Group
from drf_spectacular.utils import extend_schema_field
from typing import Optional, Dict
from rest_framework import serializers
from .models import Servicio
from tumba.models import Tumba
from difunto.models import Difunto

        
class ServicioSerializer(serializers.ModelSerializer):
    # deceased = DifuntoSerializer(read_only=True)
    # ceremonia = CeremoniaSerializer(many=True,read_only=True)
    class Meta:
        model = Servicio
        fields = '__all__'
        # [
        #     'id',
        #     'startDate',     # Campo del servicio
        #     'endDate',       # Campo del servicio
        #     'names',         # Campo del servicio
        #     'date',          # Campo del servicio
        #     'description',   # Campo del servicio
        #     'is_paid',       # Campo del servicio
        #     'amount_paid',   # Campo del servicio
        #     'payment_date',  # Campo del servicio
        #     'description',   # Campo del servicio
        #     'deceased',      # Campo del servicio
        #     'numberTomb',    # Campo del servicio
        #     'ceremonia',     # Campo del servicio
        # ]

class UserProfileSerializer(serializers.ModelSerializer): # Aquí se debe especificar many=True si es necesario
    class Meta:
        model = User
        fields = '__all__'  # O especifica los campos que necesites

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']  # Campos expuestos

class ServicioEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = [
            'startDate',     # Campo del servicio
            'endDate',       # Campo del servicio
            'ceremony',     # Campo del servicio
        ]

class DifuntoEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difunto
        fields = ['names','last_names',]

class TumbaEstadoSerializer(serializers.ModelSerializer):
    difunto = serializers.SerializerMethodField()
    servicio = ServicioEstadoSerializer(source='servicioTumba', many=True, read_only=True)

    class Meta:
        model = Tumba
        fields = ['nicheNumber', 'nicheType', 'available', 'difunto', 'servicio']
    
    @extend_schema_field(DifuntoEstadoSerializer)
    def get_difunto(self, obj) -> Optional[Dict]:
        servicio = obj.servicioTumba.order_by('-startDate').first()
        return DifuntoEstadoSerializer(servicio.deceased).data if servicio and servicio.deceased else None