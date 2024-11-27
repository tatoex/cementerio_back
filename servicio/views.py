from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ServicioSerializer, CeremoniaSerializer
from .models import Servicio, Ceremonia

# Create your views here.

class ListServiciosView(ListAPIView, CreateAPIView):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()
class DetailServicioView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()

