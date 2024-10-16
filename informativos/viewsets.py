from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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
    @action(methods=['POST'], detail=True, url_path='set-on-featured')
    def set_on_featured(self, request, pk):
        articulo = self.get_object()
        articulo.is_featured=True
        articulo.save()
        return Response ({"status":"articulo es destacado"})

    @action(methods=['POST'], detail=True, url_path='set-off-featured')
    def set_off_featured(self, request, pk):
        articulo = self.get_object()
        articulo.is_featured=False
        articulo.save()
        return Response ({"status":"articulo No es destacado"})
        
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