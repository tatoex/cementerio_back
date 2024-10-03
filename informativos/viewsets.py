from rest_framework import viewsets
from .serializers import ArticuloSerializer, GuiaSerializer, SeccionArticuloSerializer, ServicioInfoSerializer
from .models import Articulo, Guia, ServicioInfo, SeccionArticulo

class ArticuloViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ArticuloSerializer
    #definir el queryset para traer los elementos
    queryset=Articulo.objects.all()

class GuiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=GuiaSerializer
    #definir el queryset para traer los elementos
    queryset=Guia.objects.all()

class ServicioInfoViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioInfoSerializer
    #definir el queryset para traer los elementos
    queryset=ServicioInfo.objects.all()

class SeccionArticuloViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=SeccionArticuloSerializer
    #definir el queryset para traer los elementos
    queryset=SeccionArticulo.objects.all()