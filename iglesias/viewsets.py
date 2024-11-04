from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .serializers import ParroquiaSerializer, IglesiaSerializer, LinkRedSocialSerializer
from .models import Parroquia, Iglesia, LinkRedSocial
from .filters import ParroquiaFilter, IglesiaFilter, LinkRedSocialFilter

class PagionacionIgle(PageNumberPagination):
    page_size = 17
    page_size_query_param = 'page_size'
    max_page_size = 105

class ParroquiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ParroquiaSerializer
    #definir el queryset para traer los elementos
    queryset=Parroquia.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParroquiaFilter
    pagination_class = PagionacionIgle

class IglesiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=IglesiaSerializer
    #definir el queryset para traer los elementos
    queryset=Iglesia.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend]
    filterset_class = IglesiaFilter
    pagination_class = PagionacionIgle

class LinkRedSocialViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=LinkRedSocialSerializer
    #definir el queryset para traer los elementos
    queryset=LinkRedSocial.objects.all().order_by('stage_type')
    filter_backends = [DjangoFilterBackend]
    filterset_class = LinkRedSocialFilter
    pagination_class = PagionacionIgle

class ParroquiaReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ParroquiaSerializer
    #definir el queryset para traer los elementos
    queryset=Parroquia.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParroquiaFilter

class IglesiaReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=IglesiaSerializer
    #definir el queryset para traer los elementos
    queryset=Iglesia.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend]
    filterset_class = IglesiaFilter

class LinkRedSocialReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=LinkRedSocialSerializer
    #definir el queryset para traer los elementos
    queryset=LinkRedSocial.objects.all().order_by('stage_type')
    filter_backends = [DjangoFilterBackend]
    filterset_class = LinkRedSocialFilter