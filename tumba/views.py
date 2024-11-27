from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import LoteSerializer, TumbaSerializer, DisponibleTumbaSerializer
from .models import Lote, Tumba, DisponibleTumba

# Create your views here.

#decorador para hacer compatible a djrest sea compatible con esta vista
class ListTumbasView(ListAPIView, CreateAPIView ):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=TumbaSerializer
    #definir el queryset para traer los elementos
    queryset=Tumba.objects.all()
class DetailTumbaView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=TumbaSerializer
    #definir el queryset para traer los elementos
    queryset=Tumba.objects.all()

class ListLotesView(ListAPIView, CreateAPIView ):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=LoteSerializer
    #definir el queryset para traer los elementos
    queryset=Lote.objects.all()
class DetailLoteView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=LoteSerializer
    #definir el queryset para traer los elementos
    queryset=Lote.objects.all()
