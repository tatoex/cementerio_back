from rest_framework import viewsets , mixins
from django_filters.rest_framework import DjangoFilterBackend
from difunto.models import Deudo, Difunto
from tumba.models import Tumba, Lote
from servicio.models import Servicio
from obituarios.models import Obituario, Memoria, EtapasObituario
from informativos.models import Articulo, Guia, SeccionArticulo, ServicioInfo
from iglesias.models import Parroquia, Iglesia, LinkRedSocial
from .base import HistoricalActionMixin
from .serializers import (
    HistoricalDifuntoSerializer,
    HistoricalDeudoSerializer,
    HistoricalTumbaSerializer,
    HistoricalLoteSerializer,
    HistoricalServicioSerializer,
    HistoricalObituarioSerializer,
    HistoricalMemoriaSerializer,
    HistoricalEtapasObituarioSerializer,
    HistoricalArticuloSerializer,
    HistoricalGuiaSerializer,
    HistoricalServicioInfoSerializer,
    HistoricalSeccionArticuloSerializer,
    HistoricalParroquiaSerializer,
    HistoricalIglesiaSerializer,
    HistoricalLinkRedSocialSerializer,
    )
from .filters import (
    HistoricalDifuntoFilter,
    HistoricalDeudoFilter,
    HistoricalTumbaFilter,
    HistoricalLoteFilter,
    HistoricalServicioFilter,
    HistoricalObituarioFilter,
    HistoricalMemoriaFilter,
    HistoricalEtapasObituarioFilter,
    HistoricalArticuloFilter,
    HistoricalGuiaFilter,
    HistoricalServicioInfoFilter,
    HistoricalSeccionArticuloFilter,
    HistoricalParroquiaFilter,
    HistoricalIglesiaFilter,
    HistoricalLinkRedSocialFilter,
    )
from .models import (HistoricalDifunto,HistoricalDeudo,HistoricalTumba,HistoricalLote,HistoricalServicio,HistoricalObituario,HistoricalMemoria,HistoricalEtapasObituario,HistoricalArticulo,HistoricalGuia,HistoricalServicioInfo,HistoricalSeccionArticulo,HistoricalParroquia,HistoricalIglesia,HistoricalLinkRedSocial)


class HistoricalDifuntoViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalDifuntoSerializer
    queryset = HistoricalDifunto.objects.all()
    model= Difunto
    model_name:"Difunto"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalDifuntoFilter

class HistoricalDeudoViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Deudo, combinando funciones y filtros"""
    serializer_class=HistoricalDeudoSerializer
    queryset = HistoricalDeudo.objects.all()
    model= Deudo
    model_name:"Deudo"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalDeudoFilter

class HistoricalTumbaViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Tumba, combinando funciones y filtros"""
    serializer_class=HistoricalTumbaSerializer
    queryset = HistoricalTumba.objects.all()
    model= Tumba
    model_name:"Tumba"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalTumbaFilter

class HistoricalLoteViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Lote, combinando funciones y filtros"""
    serializer_class=HistoricalLoteSerializer
    queryset = HistoricalLote.objects.all()
    model= Lote
    model_name:"Lote"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalLoteFilter

class HistoricalServicioViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """ViewSet que maneja el historial del modelo Servicio, combinando funciones y filtros"""
    serializer_class = HistoricalServicioSerializer
    queryset = HistoricalServicio.objects.all()  # Cambia a objects.all() para acceder al historial
    model = Servicio
    model_name = "Servicio"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalServicioFilter

class HistoricalObituarioViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Obituario, combinando funciones y filtros"""
    serializer_class=HistoricalObituarioSerializer
    queryset = HistoricalObituario.objects.all()
    model= Obituario
    model_name:"Obituario"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalObituarioFilter

class HistoricalMemoriaViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Memoria, combinando funciones y filtros"""
    serializer_class=HistoricalMemoriaSerializer
    queryset = HistoricalMemoria.objects.all()
    model= Memoria
    model_name:"Memoria"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalMemoriaFilter

class HistoricalEtapasObituarioViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Etapas Obituario, combinando funciones y filtros"""
    serializer_class=HistoricalEtapasObituarioSerializer
    queryset = HistoricalEtapasObituario.objects.all()
    model= EtapasObituario
    model_name:"EtapasObituario"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalEtapasObituarioFilter

class HistoricalArticuloViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Articulo, combinando funciones y filtros"""
    serializer_class=HistoricalArticuloSerializer
    queryset = HistoricalArticulo.objects.all()
    model= Articulo
    model_name:"Articulo"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalArticuloFilter

class HistoricalGuiaViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Guia, combinando funciones y filtros"""
    serializer_class=HistoricalGuiaSerializer
    queryset = HistoricalGuia.objects.all()
    model= Guia
    model_name:"Guia"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalGuiaFilter

class HistoricalServicioInfoViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Servicio Informacion, combinando funciones y filtros"""
    serializer_class=HistoricalServicioInfoSerializer
    queryset = HistoricalServicioInfo.objects.all()
    model= ServicioInfo
    model_name:"ServicioInfo"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalServicioInfoFilter

class HistoricalSeccionArticuloViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Seccion Articulo, combinando funciones y filtros"""
    serializer_class=HistoricalSeccionArticuloSerializer
    queryset = HistoricalSeccionArticulo.objects.all()
    model= SeccionArticulo
    model_name:"SeccionArticulo"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalSeccionArticuloFilter

class HistoricalParroquiaViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Parroquia, combinando funciones y filtros"""
    serializer_class=HistoricalParroquiaSerializer
    queryset = HistoricalParroquia.objects.all()
    model= Parroquia
    model_name:"Parroquia"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalParroquiaFilter

class HistoricalIglesiaViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Iglesia, combinando funciones y filtros"""
    serializer_class=HistoricalIglesiaSerializer
    queryset = HistoricalIglesia.objects.all()
    model= Iglesia
    model_name:"Iglesia"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalIglesiaFilter

class HistoricalLinkRedSocialViewSet(HistoricalActionMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Link Red Social, combinando funciones y filtros"""
    serializer_class=HistoricalLinkRedSocialSerializer
    queryset = HistoricalLinkRedSocial.objects.all()
    model= LinkRedSocial
    model_name:"LinkRedSocial"
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalLinkRedSocialFilter