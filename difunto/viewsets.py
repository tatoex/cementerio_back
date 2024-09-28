from rest_framework import viewsets
from .serializers import DifuntoSerializer, DeudoSerializer
from .models import Difunto, Deudo

class DifuntoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset=Difunto.objects.all()

class DeudoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset=Deudo.objects.all()