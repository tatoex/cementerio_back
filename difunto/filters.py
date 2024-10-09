import django_filters
from .models import Difunto, Deudo
from tumba.models import Tumba

class DifuntoFilter(django_filters.FilterSet):
    names = django_filters.CharFilter(lookup_expr='icontains')  # Búsqueda insensible a mayúsculas
    last_names = django_filters.CharFilter(lookup_expr='icontains')
    idNumber = django_filters.CharFilter(lookup_expr='exact')
    requestNumber = django_filters.CharFilter(lookup_expr='exact')
    tumba = django_filters.ModelChoiceFilter(queryset=Tumba.objects.all())
    deudo = django_filters.ModelChoiceFilter(queryset=Deudo.objects.all())

    class Meta:
        model = Difunto
        fields = ['names', 'last_names', 'idNumber', 'requestNumber', 'tumba', 'deudo']


class DeudoFilter(django_filters.FilterSet):
    names = django_filters.CharFilter(lookup_expr='icontains')
    last_names = django_filters.CharFilter(lookup_expr='icontains')
    idNumber = django_filters.CharFilter(lookup_expr='exact')
    phoneNumber = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    tipo = django_filters.ChoiceFilter(choices=Deudo.TIPO_DEUDO_CHOICES)

    class Meta:
        model = Deudo
        fields = ['names', 'last_names', 'idNumber', 'phoneNumber', 'address', 'tipo']