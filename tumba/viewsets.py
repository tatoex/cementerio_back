from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TumbaSerializer, LoteSerializer, DisponibleTumbaSerializer
from .models import Tumba, Lote, DisponibleTumba


class TumbaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=TumbaSerializer
    #definir el queryset para traer los elementos
    queryset=Tumba.objects.all()
    @action(methods=['POST'], detail=True, url_path='set-on-available')
    def set_on_available(self, request, pk):
        tumba=self.get_object()
        tumba.available=True
        tumba.save()
        return Response({"status":"La tumba esta disponible"})
    @action(methods=['POST'], detail=True, url_path='set-off-available')
    def set_off_available(self, request, pk):
        tumba=self.get_object()
        tumba.available=False
        tumba.save()
        return Response({"status":"La tumba No esta disponible"})

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

