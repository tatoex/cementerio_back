import django_filters
from .models import Parroquia, Iglesia, LinkRedSocial

class IglesiaFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    parish = django_filters.ModelChoiceFilter(queryset=Parroquia.objects.all())

    class Meta:
        model = Iglesia
        fields = ['name', 'address', 'parish']

class ParroquiaFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    churches_number = django_filters.NumberFilter()

    class Meta:
        model = Parroquia
        fields = ['name', 'churches_number']

class LinkRedSocialFilter(django_filters.FilterSet):
    stage_type = django_filters.ChoiceFilter(choices=LinkRedSocial.PLATAFORMAS_CHOICES)
    iglesia = django_filters.ModelChoiceFilter(queryset=Iglesia.objects.all())
    class Meta:
        model = LinkRedSocial
        fields = ['stage_type']