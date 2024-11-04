from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DifuntoSerializer, DeudoSerializer
from .models import Difunto, Deudo
from .filters import DifuntoFilter, DeudoFilter


class DifuntoPagination(PageNumberPagination):
    page_size = 17  # Número de registros por página (puedes ajustar este valor)
    page_size_query_param = 'page_size'
    max_page_size = 100

class DifuntoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset=Difunto.objects.all().order_by('tumba')
    pagination_class = DifuntoPagination 
    filter_backends = [DjangoFilterBackend]
    filterset_class = DifuntoFilter
    
class DeudoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset=Deudo.objects.all().order_by('last_names')
    pagination_class = DifuntoPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = DeudoFilter

class DifuntoReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset=Difunto.objects.all().order_by('tumba')
    filter_backends = [DjangoFilterBackend]
    filterset_class = DifuntoFilter
    
class DeudoReadViewSet(viewsets.ReadOnlyModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset=Deudo.objects.all().order_by('last_names')
    filter_backends = [DjangoFilterBackend]
    filterset_class = DeudoFilter
    
