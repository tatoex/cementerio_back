import django_filters
from .models import Articulo, Guia, SeccionArticulo, ServicioInfo

class ArticuloFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    is_featured = django_filters.BooleanFilter()
    publication_date = django_filters.DateFilter(field_name='publication_date', lookup_expr='gte')

    class Meta:
        model = Articulo
        fields = ['title', 'author', 'is_featured', 'publication_date']

class GuiaFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Guia
        fields = ['title', 'category', 'description_short']

class SeccionArticuloFilter(django_filters.FilterSet):
    subtitle = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    article = django_filters.ModelChoiceFilter(queryset=Articulo.objects.all())

    class Meta:
        model = SeccionArticulo
        fields = ['subtitle', 'content', 'article']

class ServicioInfoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    features = django_filters.CharFilter(lookup_expr='icontains')
    exclusions = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ServicioInfo
        fields = ['title', 'category', 'features', 'exclusions']