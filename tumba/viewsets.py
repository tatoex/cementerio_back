from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TumbaSerializer, LoteSerializer, DisponibleTumbaSerializer
from .models import Tumba, Lote, DisponibleTumba
from .filters import TumbaFilter, LoteFilter, DisponibleTumbaFilter
from .utils import actualizar_estado_disponibilidad


class TumbaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=TumbaSerializer
    #definir el queryset para traer los elementos
    queryset=Tumba.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TumbaFilter
    @action(methods=['POST'], detail=True, url_path='check-available')
    def check_available(self, request, pk):
        tumba=self.get_object()
        actualizar_estado_disponibilidad(tumba)
        if tumba.available:
            return Response({'status':'La tumba esta disponible'})
        else:
            return Response({'status':'La tumba no esta disponible'})
        
class LoteViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=LoteSerializer
    #definir el queryset para traer los elementos
    queryset=Lote.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = LoteFilter

class DisponibleTumbaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DisponibleTumbaSerializer
    #definir el queryset para traer los elementos
    queryset=DisponibleTumba.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = DisponibleTumbaFilter
