from rest_framework import viewsets
from .serializers import ParroquiaSerializer, IglesiaSerializer, LinkRedSocialSerializer
from .models import Parroquia, Iglesia, LinkRedSocial

class ParroquiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ParroquiaSerializer
    #definir el queryset para traer los elementos
    queryset=Parroquia.objects.all()

class IglesiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=IglesiaSerializer
    #definir el queryset para traer los elementos
    queryset=Iglesia.objects.all()

class LinkRedSocialViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=LinkRedSocialSerializer
    #definir el queryset para traer los elementos
    queryset=LinkRedSocial.objects.all()