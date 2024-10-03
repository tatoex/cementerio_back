from rest_framework import viewsets
from .serializers import ObituarioSerializer, MemoriaSerializer, EtapasObituarioSerializer
from .models import Obituario, Memoria, EtapasObituario

class ObituarioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=Obituario.objects.all()

class MemoriaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=MemoriaSerializer
    #definir el queryset para traer los elementos
    queryset=Memoria.objects.all()

class EtapasObituarioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=EtapasObituarioSerializer
    #definir el queryset para traer los elementos
    queryset=EtapasObituario.objects.all()