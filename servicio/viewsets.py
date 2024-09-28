from rest_framework import viewsets
from .serializers import ServicioSerializer, CeremoniaSerializer
from .models import Servicio, Ceremonia

class ServicioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()

class CeremoniaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=CeremoniaSerializer
    #definir el queryset para traer los elementos
    queryset=Ceremonia.objects.all()