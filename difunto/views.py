# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import DifuntoSerializer, DeudoSerializer
from .models import Difunto, Deudo

# Create your views here.

class ListDifuntosView(ListAPIView, CreateAPIView):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset= Difunto.objects.all()
class DetailDifuntoView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset= Difunto.objects.all()

class ListDeudosView(ListAPIView, CreateAPIView):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset= Deudo.objects.all()
class DetailDeudoView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset= Deudo.objects.all()

