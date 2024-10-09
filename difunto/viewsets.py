from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DifuntoSerializer, DeudoSerializer
from .models import Difunto, Deudo
from .filters import DifuntoFilter, DeudoFilter

class DifuntoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset=Difunto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = DifuntoFilter

    

class DeudoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset=Deudo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = DeudoFilter
