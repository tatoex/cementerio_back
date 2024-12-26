from rest_framework.routers import DefaultRouter
from .viewsets import (
    ObituarioViewSet,
    ObituarioReadViewSet,
    MemoriaViewSet,
    MemoriaReadViewSet,
    EtapasObituarioReadViewSet,
    EtapasObituarioViewSet,
)

router=DefaultRouter()
router.register(r'obituario',ObituarioViewSet, basename='obituario')
router.register(r'obituarioread',ObituarioReadViewSet, basename='obituarioread')
router.register(r'memoria',MemoriaViewSet, basename='memoria')
router.register(r'memoriaread',MemoriaReadViewSet, basename='memoriaread')
router.register(r'etapa',EtapasObituarioViewSet, basename='etapa')
router.register(r'etaparead',EtapasObituarioReadViewSet, basename='etaparead')


urlpatterns = router.urls
