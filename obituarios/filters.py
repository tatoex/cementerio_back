import django_filters

from difunto.models import Difunto
from servicio.models import Servicio
from .models import Obituario, Memoria, EtapasObituario

class ObituarioFilter(django_filters.FilterSet):
    place = django_filters.CharFilter(lookup_expr='icontains')
    cementery = django_filters.CharFilter(lookup_expr='icontains')
    deceased = django_filters.ModelChoiceFilter(queryset=Difunto.objects.all())

    class Meta:
        model = Obituario
        fields = ['place', 'cementery', 'deceased']

class MemoriaFilter(django_filters.FilterSet):
    names = django_filters.CharFilter(lookup_expr='icontains')
    relationship = django_filters.CharFilter(lookup_expr='icontains')
    obituary = django_filters.ModelChoiceFilter(queryset=Obituario.objects.all())

    class Meta:
        model = Memoria
        fields = ['names', 'relationship', 'obituary']

import django_filters
from .models import EtapasObituario

class EtapasObituarioFilter(django_filters.FilterSet):
    stage_ceremony = django_filters.ChoiceFilter(choices=EtapasObituario.ETAPAS_OBITUARIO_CHOICES)
    place = django_filters.CharFilter(lookup_expr='icontains')
    obituary = django_filters.ModelChoiceFilter(queryset=Obituario.objects.all())
    ceremony = django_filters.ModelChoiceFilter(queryset=Servicio.objects.all())

    class Meta:
        model = EtapasObituario
        fields = ['stage_ceremony', 'place', 'obituary', 'ceremony']