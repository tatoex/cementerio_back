from rest_framework.routers import DefaultRouter
from .viewsets import ArticuloViewSet, SeccionArticuloViewSet, ServicioInfoViewSet, GuiaViewSet

router=DefaultRouter()

router.register(r'articulo',ArticuloViewSet, basename='articulo')
router.register(r'seccion',SeccionArticuloViewSet, basename='seccion')
router.register(r'info',ServicioInfoViewSet, basename='info')
router.register(r'guia',GuiaViewSet, basename='guia')


urlpatterns = router.urls
