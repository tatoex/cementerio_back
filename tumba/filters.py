import django_filters
from .models import DisponibleTumba, Lote, Tumba

class TumbaFilter(django_filters.FilterSet):
    nicheNumber = django_filters.NumberFilter()
    nicheNumber_gt = django_filters.NumberFilter(field_name='nicheNumber', lookup_expr='gt')
    nicheNumber_lt = django_filters.NumberFilter(field_name='nicheNumber', lookup_expr='lt')
    nicheType = django_filters.ChoiceFilter(choices=Tumba.TIPO_NICHO_CHOICES)
    available = django_filters.BooleanFilter()
    nameLote = django_filters.ModelChoiceFilter(queryset=Lote.objects.all())

    class Meta:
        model = Tumba
        fields = ['nicheNumber', 'nicheType', 'available', 'nameLote']

class LoteFilter(django_filters.FilterSet):
    blockName = django_filters.NumberFilter(lookup_expr='exact')  # Búsqueda exacta por número de bloque
    typeblock = django_filters.CharFilter(lookup_expr='icontains')  # Búsqueda por tipo de bloque
    numbersblock = django_filters.NumberFilter(lookup_expr='exact')  # Búsqueda por número exacto de tipo de bloque
    filas = django_filters.NumberFilter(lookup_expr='exact')  # Búsqueda por número de filas
    columnas = django_filters.NumberFilter(lookup_expr='exact')  # Búsqueda por número de columnas
    limite = django_filters.NumberFilter(lookup_expr='exact')  # Búsqueda por el límite de espacio

    class Meta:
        model = Lote
        fields = ['blockName', 'typeblock', 'numbersblock', 'filas', 'columnas', 'limite']

class DisponibleTumbaFilter(django_filters.FilterSet):
    startDate = django_filters.DateFilter(field_name='startDate', lookup_expr='gte')  # Fecha mayor o igual a
    endDate = django_filters.DateFilter(field_name='endDate', lookup_expr='lte')  # Fecha menor o igual a
    numberTumba = django_filters.ModelChoiceFilter(queryset=Tumba.objects.all())  # Filtra por tumba específica

    class Meta:
        model = DisponibleTumba
        fields = ['startDate', 'endDate', 'numberTumba']