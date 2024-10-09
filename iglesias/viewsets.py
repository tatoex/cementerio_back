from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ParroquiaSerializer, IglesiaSerializer, LinkRedSocialSerializer
from .models import Parroquia, Iglesia, LinkRedSocial
from .filters import ParroquiaFilter, IglesiaFilter, LinkRedSocialFilter

class ParroquiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ParroquiaSerializer
    #definir el queryset para traer los elementos
    queryset=Parroquia.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParroquiaFilter

class IglesiaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=IglesiaSerializer
    #definir el queryset para traer los elementos
    queryset=Iglesia.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = IglesiaFilter

class LinkRedSocialViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=LinkRedSocialSerializer
    #definir el queryset para traer los elementos
    queryset=LinkRedSocial.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = LinkRedSocialFilter