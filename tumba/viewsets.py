from rest_framework import viewsets
from .serializers import TumbaSerializer, LoteSerializer, DisponibleTumbaSerializer
from .models import Tumba, Lote, DisponibleTumba

class TumbaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=TumbaSerializer
    #definir el queryset para traer los elementos
    queryset=Tumba.objects.all()

class LoteViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=LoteSerializer
    #definir el queryset para traer los elementos
    queryset=Lote.objects.all()


class DisponibleTumbaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=DisponibleTumbaSerializer
    #definir el queryset para traer los elementos
    queryset=DisponibleTumba.objects.all()