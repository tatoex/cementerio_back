from rest_framework import viewsets
from difunto.models import Deudo, Difunto
from tumba.models import Tumba, Lote, DisponibleTumba
from servicio.models import Servicio, Ceremonia
from obituarios.models import Obituario, Memoria, EtapasObituario
from informativos.models import Articulo, Guia, SeccionArticulo, ServicioInfo
from iglesias.models import Parroquia, Iglesia, LinkRedSocial
from .base import HistoricalActionMixin, HistoricalQuerySetMixin
from .serializers import (
    HistoricalDifuntoSerializer,
    HistoricalDeudoSerializer,
    HistoricalTumbaSerializer,
    HistoricalLoteSerializer,
    HistoricalDisponibleTumbaSerializer,
    HistoricalServicioSerializer,
    HistoricalCeremoniaSerializer,
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

class HistoricalDifuntoViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalDifuntoSerializer
    model= Difunto
    model_name:"Difunto"

class HistoricalDeudoViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Deudo, combinando funciones y filtros"""
    serializer_class=HistoricalDeudoSerializer
    model= Deudo
    model_name:"Deudo"

class HistoricalTumbaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Tumba, combinando funciones y filtros"""
    serializer_class=HistoricalTumbaSerializer
    model= Tumba
    model_name:"Tumba"

class HistoricalLoteViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Lote, combinando funciones y filtros"""
    serializer_class=HistoricalLoteSerializer
    model= Lote
    model_name:"Lote"

class HistoricalDisponibleTumbaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Disponible, combinando funciones y filtros"""
    serializer_class=HistoricalDisponibleTumbaSerializer
    model= DisponibleTumba
    model_name:"DisponibleTumba"

class HistoricalServicioViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Servicio, combinando funciones y filtros"""
    serializer_class=HistoricalServicioSerializer
    model= Servicio
    model_name:"Servicio"

class HistoricalCeremoniaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Ceremonia, combinando funciones y filtros"""
    serializer_class=HistoricalCeremoniaSerializer
    model= Ceremonia
    model_name:"Ceremonia"

class HistoricalObituarioViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Obituario, combinando funciones y filtros"""
    serializer_class=HistoricalObituarioSerializer
    model= Obituario
    model_name:"Obituario"

class HistoricalMemoriaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Memoria, combinando funciones y filtros"""
    serializer_class=HistoricalMemoriaSerializer
    model= Memoria
    model_name:"Memoria"

class HistoricalEtapasObituarioViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Etapas Obituario, combinando funciones y filtros"""
    serializer_class=HistoricalEtapasObituarioSerializer
    model= EtapasObituario
    model_name:"EtapasObituario"

class HistoricalArticuloViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Articulo, combinando funciones y filtros"""
    serializer_class=HistoricalArticuloSerializer
    model= Articulo
    model_name:"Articulo"

class HistoricalGuiaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Guia, combinando funciones y filtros"""
    serializer_class=HistoricalGuiaSerializer
    model= Guia
    model_name:"Guia"

class HistoricalServicioInfoViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Servicio Informacion, combinando funciones y filtros"""
    serializer_class=HistoricalServicioInfoSerializer
    model= ServicioInfo
    model_name:"ServicioInfo"

class HistoricalSeccionArticuloViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Seccion Articulo, combinando funciones y filtros"""
    serializer_class=HistoricalSeccionArticuloSerializer
    model= SeccionArticulo
    model_name:"SeccionArticulo"

class HistoricalParroquiaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Parroquia, combinando funciones y filtros"""
    serializer_class=HistoricalParroquiaSerializer
    model= Parroquia
    model_name:"Parroquia"

class HistoricalIglesiaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Iglesia, combinando funciones y filtros"""
    serializer_class=HistoricalIglesiaSerializer
    model= Iglesia
    model_name:"Iglesia"

class HistoricalLinkRedSocialViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Link Red Social, combinando funciones y filtros"""
    serializer_class=HistoricalLinkRedSocialSerializer
    model= LinkRedSocial
    model_name:"LinkRedSocial"