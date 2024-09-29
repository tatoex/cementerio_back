from rest_framework.routers import DefaultRouter
from .viewsets import (
    HistoricalDifuntoViewSet,
    HistoricalDeudoViewSet,
    HistoricalLoteViewSet,
    HistoricalTumbaViewSet,
    HistoricalDisponibleTumbaViewSet,
    HistoricalServicioViewSet,
    HistoricalCeremoniaViewSet,
)
router=DefaultRouter()
router.register(r'difunto-history',HistoricalDifuntoViewSet, basename='difunto-history')
router.register(r'deudo-history',HistoricalDeudoViewSet, basename='deudo-history')
router.register(r'lote-history',HistoricalLoteViewSet, basename='lote-history')
router.register(r'tumba-history',HistoricalTumbaViewSet, basename='tumba-history')
router.register(r'disponible-tumba-history',HistoricalDisponibleTumbaViewSet, basename='disponible-tumba-history')
router.register(r'servicio-history',HistoricalServicioViewSet, basename='servicio-history')
router.register(r'ceremonia-history',HistoricalCeremoniaViewSet, basename='ceremonia-history')

urlpatterns = router.urls
