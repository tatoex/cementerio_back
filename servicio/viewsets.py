from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ServicioSerializer, CeremoniaSerializer
from .models import Servicio, Ceremonia
from .filters import ServicioFilter, CeremoniaFilter
from .utils import sincronizar_disponibilidad_tumba

class ServicioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServicioFilter
    
    @action(methods=['POST'], detail=True, url_path='sincronizar-disponibilidad')
    def sincronizar_disponibilidad(self, request, pk=None):
        """accion para sincronizar las fechas de Disponibilidad de la tumba basado en funcion a servicio"""
        servicio=self.get_object()
        sincronizar_disponibilidad_tumba(servicio)
        return Response({'status':'Fechas sincronizadas :)'}, status=status.HTTP_200_OK)

class CeremoniaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=CeremoniaSerializer
    #definir el queryset para traer los elementos
    queryset=Ceremonia.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CeremoniaFilter

