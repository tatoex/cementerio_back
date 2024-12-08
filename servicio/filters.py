import django_filters
from django_filters import rest_framework as filters
from difunto.models import  Difunto
from tumba.filters import TumbaFilter
from tumba.models import Tumba, Lote
from .models import Servicio


class ServicioFilter(django_filters.FilterSet):
    startDate = django_filters.DateFilter(field_name='startDate', lookup_expr='gte')  # Fecha mayor o igual a
    endDate = django_filters.DateFilter(field_name='endDate', lookup_expr='lte')  # Fecha menor o igual a
    ceremony = django_filters.ChoiceFilter(choices=Servicio.TIPO_CEREMONIA_CHOICES)
    numberTomb = django_filters.ModelChoiceFilter(queryset=Tumba.objects.all())
    deceased = django_filters.ModelChoiceFilter(queryset=Difunto.objects.all())

    

    class Meta:
        model = Servicio
        fields = ['startDate', 'endDate','ceremony', 'numberTomb', 'deceased']
        
from django.db.models import Q
from .models import Tumba, Servicio, Difunto

class TumbaEstadoFilter(django_filters.FilterSet):
    nicheNumber = django_filters.NumberFilter()
    nicheType = django_filters.ChoiceFilter(choices=Tumba.TIPO_NICHO_CHOICES)
    available = django_filters.BooleanFilter()
    nameLote = django_filters.ModelChoiceFilter(queryset=Lote.objects.all())
    nombre_difunto = django_filters.CharFilter(method='filter_nombre_difunto', label="Nombre del Difunto")
    apellido_difunto = django_filters.CharFilter(method='filter_apellido_difunto', label="Apellido del Difunto")
    
    class Meta:
        model = Tumba
        fields = ['nicheNumber', 'nicheType', 'available', 'nameLote', 'nombre_difunto', 'apellido_difunto']

    def filter_nombre_difunto(self, queryset, name, value):
        # Filtrar por coincidencia exacta del nombre del difunto
        return queryset.filter(servicioTumba__deceased__names__iexact=value).distinct()

    def filter_apellido_difunto(self, queryset, name, value):
        # Filtrar por coincidencia exacta del apellido del difunto
        return queryset.filter(servicioTumba__deceased__last_names__iexact=value).distinct()