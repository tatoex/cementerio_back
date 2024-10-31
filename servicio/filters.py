import django_filters

from difunto.models import  Difunto
from tumba.models import Tumba
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
        
