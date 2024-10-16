from rest_framework.routers import DefaultRouter
from .viewsets import ObituarioViewSet, MemoriaViewSet, EtapasObituarioViewSet

router=DefaultRouter()
router.register(r'obituario',ObituarioViewSet, basename='obituario')
router.register(r'memoria',MemoriaViewSet, basename='memoria')
router.register(r'etapa',EtapasObituarioViewSet, basename='etapa')


urlpatterns = router.urls
