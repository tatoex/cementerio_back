import django_filters

from difunto.models import Deudo, Difunto
from tumba.models import Tumba
from .models import Servicio, Ceremonia


class ServicioFilter(django_filters.FilterSet):
    startDate = django_filters.DateFilter(field_name='startDate', lookup_expr='gte')  # Fecha mayor o igual a
    endDate = django_filters.DateFilter(field_name='endDate', lookup_expr='lte')  # Fecha menor o igual a
    numberTomb = django_filters.ModelChoiceFilter(queryset=Tumba.objects.all())
    deceased = django_filters.ModelChoiceFilter(queryset=Difunto.objects.all())
    deudo = django_filters.ModelChoiceFilter(queryset=Deudo.objects.all())

    class Meta:
        model = Servicio
        fields = ['startDate', 'endDate', 'numberTomb', 'deceased', 'deudo']
        
class CeremoniaFilter(django_filters.FilterSet):
    names = django_filters.ChoiceFilter(choices=Ceremonia.TIPO_CEREMONIA_CHOICES)
    date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    servicios = django_filters.ModelChoiceFilter(queryset=Servicio.objects.all())

    class Meta:
        model = Ceremonia
        fields = ['names', 'date', 'servicios']