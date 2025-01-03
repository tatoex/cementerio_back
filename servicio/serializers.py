from django.contrib.auth.models import User, Group
from drf_spectacular.utils import extend_schema_field
from typing import Optional, Dict
from rest_framework import serializers
from .models import Servicio
from tumba.models import Tumba
from difunto.models import Difunto

        
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'



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
        fields = ['nicheNumber', 'nicheType', 'available','nameLote', 'difunto', 'servicio']
    
    @extend_schema_field(DifuntoEstadoSerializer)
    def get_difunto(self, obj) -> Optional[Dict]:
        servicio = obj.servicioTumba.order_by('-startDate').first()
        return DifuntoEstadoSerializer(servicio.deceased).data if servicio and servicio.deceased else None
    

class ServicioReporteSerializer(serializers.Serializer):
    ceremony = serializers.CharField()
    activos = serializers.IntegerField()
    completados = serializers.IntegerField()
    pendiente_pago = serializers.IntegerField()