from rest_framework import viewsets
from difunto.models import Deudo, Difunto
from tumba.models import Tumba, Lote, DisponibleTumba
from servicio.models import Servicio, Ceremonia
from .base import HistoricalActionMixin, HistoricalQuerySetMixin
from .serializers import (
    HistoricalDifuntoSerializer,
    HistoricalDeudoSerializer,
    HistoricalTumbaSerializer,
    HistoricalLoteSerializer,
    HistoricalDisponibleTumbaSerializer,
    HistoricalServicioSerializer,
    HistoricalCeremoniaSerializer
    )

class HistoricalDifuntoViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalDifuntoSerializer
    model= Difunto
    model_name:"Difunto"

class HistoricalDeudoViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalDeudoSerializer
    model= Deudo
    model_name:"Deudo"

class HistoricalTumbaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalTumbaSerializer
    model= Tumba
    model_name:"Tumba"

class HistoricalLoteViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalLoteSerializer
    model= Lote
    model_name:"Lote"

class HistoricalDisponibleTumbaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalDisponibleTumbaSerializer
    model= DisponibleTumba
    model_name:"DisponibleTumba"

class HistoricalServicioViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalServicioSerializer
    model= Servicio
    model_name:"Servicio"

class HistoricalCeremoniaViewSet(HistoricalActionMixin,HistoricalQuerySetMixin, viewsets.ReadOnlyModelViewSet):
    """viewset se encarga de manejar el historial del modelo Difunto, combinando funciones y filtros"""
    serializer_class=HistoricalCeremoniaSerializer
    model= Ceremonia
    model_name:"Ceremonia"