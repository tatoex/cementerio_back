from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LoteOcupacionSerializer, TumbaSerializer, LoteSerializer
from .models import Tumba, Lote
from .filters import TumbaFilter, LoteFilter

class PagionacionTumba(PageNumberPagination):
    page_size = 17
    page_size_query_param = 'page_size'
    max_page_size = 105

class TumbaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=TumbaSerializer
    #definir el queryset para traer los elementos
    queryset=Tumba.objects.all().order_by('nameLote')
    filter_backends = [DjangoFilterBackend]
    filterset_class = TumbaFilter
    pagination_class = PagionacionTumba

    @action(methods=['POST'], detail=True, url_path='set-on-available')
    def set_on_available(self, request, pk):
        tumba = self.get_object()
        tumba.available=True
        tumba.save()
        return Response ({"status":"El espacio esta disponible"})
    @action(methods=['POST'], detail=True, url_path='set-off-available')
    def set_off_available(self, request, pk):
        tumba = self.get_object()
        tumba.available=False
        tumba.save()
        return Response ({"status":"El espacio No esta disponible"})
        
class LoteViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=LoteSerializer
    #definir el queryset para traer los elementos
    queryset=Lote.objects.all().order_by('blockName')
     # Agregamos el backend de filtros y el filtro correspondiente
    filter_backends = [DjangoFilterBackend]
    filterset_class = LoteFilter
    pagination_class = PagionacionTumba

# ViewSet de solo lectura para Tumba
class TumbaReadViewSet(viewsets.ReadOnlyModelViewSet):
    # Configuramos el serializer para todos los métodos
    serializer_class = TumbaSerializer
    # Definimos el queryset para traer todos los elementos
    queryset = Tumba.objects.all().order_by('nameLote')
    # Agregamos el backend de filtros y el filtro correspondiente
    filter_backends = [DjangoFilterBackend]
    filterset_class = TumbaFilter
    # Agregamos la configuración de paginación personalizada

# ViewSet de solo lectura para Tumba
class LoteReadViewSet(viewsets.ReadOnlyModelViewSet):
    # Configuramos el serializer para todos los métodos
    serializer_class = TumbaSerializer
    # Definimos el queryset para traer todos los elementos
    queryset = Lote.objects.all().order_by('blockName')
    # Agregamos el backend de filtros y el filtro correspondiente
    filter_backends = [DjangoFilterBackend]
    filterset_class = LoteFilter
    # Agregamos la configuración de paginación personalizada

class OcupacionLoteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LoteOcupacionSerializer
    queryset = Lote.objects.all()  # La consulta no necesita agregaciones adicionales
    filter_backends = [DjangoFilterBackend]
    filterset_class = LoteFilter