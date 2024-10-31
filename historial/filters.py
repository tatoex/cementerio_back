import django_filters
from difunto.models import Difunto, Deudo
# from tumba.models import Tumba, Lote
# from servicio.models import Servicio
# from obituarios.models import Obituario, Memoria, EtapasObituario
# from iglesias.models import Parroquia, Iglesia, LinkRedSocial
# from informativos.models import Articulo, Guia, ServicioInfo, SeccionArticulo
from difunto.filters import DifuntoFilter, DeudoFilter
from tumba.filters import TumbaFilter, LoteFilter
from servicio.filters import ServicioFilter
from obituarios.filters import ObituarioFilter, MemoriaFilter, EtapasObituarioFilter
from iglesias.filters import ParroquiaFilter, IglesiaFilter, LinkRedSocialFilter
from informativos.filters import ArticuloFilter, GuiaFilter, ServicioInfoFilter, SeccionArticuloFilter
from .models import (HistoricalDifunto,HistoricalDeudo,HistoricalTumba,HistoricalLote,HistoricalServicio,HistoricalObituario,HistoricalMemoria,HistoricalEtapasObituario,HistoricalArticulo,HistoricalGuia,HistoricalServicioInfo,HistoricalSeccionArticulo,HistoricalParroquia,HistoricalIglesia,HistoricalLinkRedSocial)


# Filtro genérico para el historial
class HistoricalFilter(django_filters.FilterSet):
    """Filtro genérico para todos los modelos históricos"""
    start_date = django_filters.DateTimeFilter(field_name="history_date", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="history_date", lookup_expr='lte')
    entity_id = django_filters.NumberFilter(field_name="id")
    history_type = django_filters.CharFilter(field_name="history_type")
    user= django_filters.NumberFilter(field_name="history_user")

    class Meta:
        model = None  # Se definirá en cada clase hija
        fields = ['start_date', 'end_date', 'entity_id', 'history_type', 'user']

class HistoricalDifuntoFilter(DifuntoFilter, HistoricalFilter):
    """Filtro para el historial del modelo Difunto, combinando los filtros de Difunto y los generales"""

    class Meta(DifuntoFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalDifunto
        fields = HistoricalFilter.Meta.fields + DifuntoFilter.Meta.fields

# Filtro específico para Deudo en el historial
class HistoricalDeudoFilter(DeudoFilter, HistoricalFilter):
    """Filtro para el historial del modelo Deudo, combinando los filtros de Deudo y los generales"""

    class Meta(DeudoFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalDeudo
        fields = HistoricalFilter.Meta.fields + DeudoFilter.Meta.fields

# Filtro específico para Tumba en el historial
class HistoricalTumbaFilter(TumbaFilter, HistoricalFilter):
    """Filtro para el historial del modelo Tumba, combinando los filtros de Tumba y los generales"""

    class Meta(TumbaFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalTumba
        fields = HistoricalFilter.Meta.fields + TumbaFilter.Meta.fields

# Filtro específico para Lote en el historial
class HistoricalLoteFilter(LoteFilter, HistoricalFilter):
    """Filtro para el historial del modelo Lote, combinando los filtros de Lote y los generales"""

    class Meta(LoteFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalLote
        fields = HistoricalFilter.Meta.fields + LoteFilter.Meta.fields

# Filtro específico para Servicio en el historial
class HistoricalServicioFilter(ServicioFilter, HistoricalFilter):
    """Filtro para el historial del modelo Servicio, combinando los filtros de Servicio y los generales"""

    class Meta(ServicioFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalServicio
        fields = HistoricalFilter.Meta.fields + ServicioFilter.Meta.fields


# Filtro específico para Obituario en el historial
class HistoricalObituarioFilter(ObituarioFilter, HistoricalFilter):
    """Filtro para el historial del modelo Obituario, combinando los filtros de Obituario y los generales"""

    class Meta(ObituarioFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalObituario
        fields = HistoricalFilter.Meta.fields + ObituarioFilter.Meta.fields

# Filtro específico para Memoria en el historial
class HistoricalMemoriaFilter(MemoriaFilter, HistoricalFilter):
    """Filtro para el historial del modelo Memoria, combinando los filtros de Memoria y los generales"""

    class Meta(MemoriaFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalMemoria
        fields = HistoricalFilter.Meta.fields + MemoriaFilter.Meta.fields

# Filtro específico para EtapasObituario en el historial
class HistoricalEtapasObituarioFilter(EtapasObituarioFilter, HistoricalFilter):
    """Filtro para el historial del modelo EtapasObituario, combinando los filtros de EtapasObituario y los generales"""

    class Meta(EtapasObituarioFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalEtapasObituario
        fields = HistoricalFilter.Meta.fields + EtapasObituarioFilter.Meta.fields

# Filtro específico para Articulo en el historial
class HistoricalArticuloFilter(ArticuloFilter, HistoricalFilter):
    """Filtro para el historial del modelo Articulo, combinando los filtros de Articulo y los generales"""

    class Meta(ArticuloFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalArticulo
        fields = HistoricalFilter.Meta.fields + ArticuloFilter.Meta.fields

# Filtro específico para Guia en el historial
class HistoricalGuiaFilter(GuiaFilter, HistoricalFilter):
    """Filtro para el historial del modelo Guia, combinando los filtros de Guia y los generales"""

    class Meta(GuiaFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalGuia
        fields = HistoricalFilter.Meta.fields + GuiaFilter.Meta.fields

# Filtro específico para ServicioInfo en el historial
class HistoricalServicioInfoFilter(ServicioInfoFilter, HistoricalFilter):
    """Filtro para el historial del modelo ServicioInfo, combinando los filtros de ServicioInfo y los generales"""

    class Meta(ServicioInfoFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalServicioInfo
        fields = HistoricalFilter.Meta.fields + ServicioInfoFilter.Meta.fields

# Filtro específico para SeccionArticulo en el historial
class HistoricalSeccionArticuloFilter(SeccionArticuloFilter, HistoricalFilter):
    """Filtro para el historial del modelo SeccionArticulo, combinando los filtros de SeccionArticulo y los generales"""

    class Meta(SeccionArticuloFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalSeccionArticulo
        fields = HistoricalFilter.Meta.fields + SeccionArticuloFilter.Meta.fields

# Filtro específico para Parroquia en el historial
class HistoricalParroquiaFilter(ParroquiaFilter, HistoricalFilter):
    """Filtro para el historial del modelo Parroquia, combinando los filtros de Parroquia y los generales"""

    class Meta(ParroquiaFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalParroquia
        fields = HistoricalFilter.Meta.fields + ParroquiaFilter.Meta.fields

# Filtro específico para Iglesia en el historial
class HistoricalIglesiaFilter(IglesiaFilter, HistoricalFilter):
    """Filtro para el historial del modelo Iglesia, combinando los filtros de Iglesia y los generales"""

    class Meta(IglesiaFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalIglesia
        fields = HistoricalFilter.Meta.fields + IglesiaFilter.Meta.fields

# Filtro específico para LinkRedSocial en el historial
class HistoricalLinkRedSocialFilter(LinkRedSocialFilter, HistoricalFilter):
    """Filtro para el historial del modelo LinkRedSocial, combinando los filtros de LinkRedSocial y los generales"""

    class Meta(LinkRedSocialFilter.Meta, HistoricalFilter.Meta):
        model = HistoricalLinkRedSocial
        fields = HistoricalFilter.Meta.fields + LinkRedSocialFilter.Meta.fields