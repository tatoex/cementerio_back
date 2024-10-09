from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ObituarioSerializer, MemoriaSerializer, EtapasObituarioSerializer
from .models import Obituario, Memoria, EtapasObituario
from .filters import ObituarioFilter, MemoriaFilter, EtapasObituarioFilter

class ObituarioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=Obituario.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ObituarioFilter

class MemoriaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=MemoriaSerializer
    #definir el queryset para traer los elementos
    queryset=Memoria.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MemoriaFilter

class EtapasObituarioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=EtapasObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=EtapasObituario.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = EtapasObituarioFilter