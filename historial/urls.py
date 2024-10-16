from rest_framework.routers import DefaultRouter
from .viewsets import (
    HistoricalDifuntoViewSet,
    HistoricalDeudoViewSet,
    HistoricalLoteViewSet,
    HistoricalTumbaViewSet,
    HistoricalServicioViewSet,
    HistoricalArticuloViewSet,
    HistoricalSeccionArticuloViewSet,
    HistoricalServicioInfoViewSet,
    HistoricalGuiaViewSet,
    HistoricalObituarioViewSet,
    HistoricalMemoriaViewSet,
    HistoricalEtapasObituarioViewSet,
    HistoricalParroquiaViewSet,
    HistoricalIglesiaViewSet,
    HistoricalLinkRedSocialViewSet,
)
router=DefaultRouter()
router.register(r'difunto-history',HistoricalDifuntoViewSet, basename='difunto-history')
router.register(r'deudo-history',HistoricalDeudoViewSet, basename='deudo-history')
router.register(r'lote-history',HistoricalLoteViewSet, basename='lote-history')
router.register(r'tumba-history',HistoricalTumbaViewSet, basename='tumba-history')
router.register(r'servicio-history',HistoricalServicioViewSet, basename='servicio-history')
router.register(r'articulo-history',HistoricalArticuloViewSet, basename='articulo-history')
router.register(r'seccion-history',HistoricalSeccionArticuloViewSet, basename='seccion-history')
router.register(r'info-history',HistoricalServicioInfoViewSet, basename='info-history')
router.register(r'guia-history',HistoricalGuiaViewSet, basename='guia-history')
router.register(r'obituario-history',HistoricalObituarioViewSet, basename='obituario-history')
router.register(r'memoria-history',HistoricalMemoriaViewSet, basename='memoria-history')
router.register(r'etapas-history',HistoricalEtapasObituarioViewSet, basename='etapas-history')
router.register(r'parroquia-history',HistoricalParroquiaViewSet, basename='parroquia-history')
router.register(r'iglesia-history',HistoricalIglesiaViewSet, basename='iglesia-history')
router.register(r'social-history',HistoricalLinkRedSocialViewSet, basename='social-history')

urlpatterns = router.urls
