from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .serializers import ObituarioSerializer, MemoriaSerializer, EtapasObituarioSerializer
from .models import Obituario, Memoria, EtapasObituario
from .filters import ObituarioFilter, MemoriaFilter, EtapasObituarioFilter

class PagionacionObituario(PageNumberPagination):
    page_size = 17
    page_size_query_param = 'page_size'
    max_page_size = 105

class ObituarioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=Obituario.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ObituarioFilter
    pagination_class = PagionacionObituario

class ObituarioReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=Obituario.objects.all().order_by('date')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ObituarioFilter


class MemoriaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=MemoriaSerializer
    #definir el queryset para traer los elementos
    queryset=Memoria.objects.all().order_by('date')
    filter_backends = [DjangoFilterBackend]
    filterset_class = MemoriaFilter
    pagination_class = PagionacionObituario

class MemoriaReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=MemoriaSerializer
    #definir el queryset para traer los elementos
    queryset=Memoria.objects.all().order_by('date')
    filter_backends = [DjangoFilterBackend]
    filterset_class = MemoriaFilter


class EtapasObituarioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=EtapasObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=EtapasObituario.objects.all().order_by('date')
    filter_backends = [DjangoFilterBackend]
    filterset_class = EtapasObituarioFilter
    pagination_class = PagionacionObituario

class EtapasObituarioReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=EtapasObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=EtapasObituario.objects.all().order_by('date')
    filter_backends = [DjangoFilterBackend]
    filterset_class = EtapasObituarioFilter


