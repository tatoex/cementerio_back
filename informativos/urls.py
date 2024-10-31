from rest_framework.routers import DefaultRouter
from .viewsets import ArticuloViewSet, ArticuloReadViewSet, SeccionArticuloViewSet, SeccionArticuloReadViewSet, ServicioInfoViewSet,ServicioInfoReadViewSet, GuiaViewSet, GuiaReadViewSet

router=DefaultRouter()

router.register(r'articulo',ArticuloViewSet, basename='articulo')
router.register(r'articuloread',ArticuloReadViewSet, basename='articuloread')
router.register(r'seccion',SeccionArticuloViewSet, basename='seccion')
router.register(r'seccionread',SeccionArticuloReadViewSet, basename='seccionread')
router.register(r'info',ServicioInfoViewSet, basename='info')
router.register(r'inforead',ServicioInfoReadViewSet, basename='inforead')
router.register(r'guia',GuiaViewSet, basename='guia')
router.register(r'guiaread',GuiaReadViewSet, basename='guiaread')


urlpatterns = router.urls
