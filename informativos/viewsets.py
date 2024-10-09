from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ArticuloSerializer, GuiaSerializer, SeccionArticuloSerializer, ServicioInfoSerializer
from .models import Articulo, Guia, ServicioInfo, SeccionArticulo
from .filters import ArticuloFilter, GuiaFilter, ServicioInfoFilter, SeccionArticuloFilter

class ArticuloViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ArticuloSerializer
    #definir el queryset para traer los elementos
    queryset=Articulo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticuloFilter

class GuiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=GuiaSerializer
    #definir el queryset para traer los elementos
    queryset=Guia.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = GuiaFilter

class ServicioInfoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioInfoSerializer
    #definir el queryset para traer los elementos
    queryset=ServicioInfo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServicioInfoFilter

class SeccionArticuloViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=SeccionArticuloSerializer
    #definir el queryset para traer los elementos
    queryset=SeccionArticulo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SeccionArticuloFilter