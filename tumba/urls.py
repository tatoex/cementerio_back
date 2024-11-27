from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import OcupacionLoteViewSet, TumbaViewSet, TumbaReadViewSet, LoteViewSet, LoteReadViewSet


router = DefaultRouter()
router.register(r'tumba', TumbaViewSet, basename='tumba')
router.register(r'tumbaread', TumbaReadViewSet, basename='tumbaread')
router.register(r'lote', LoteViewSet, basename='lote')
router.register(r'loteread', LoteReadViewSet, basename='loteread')
router.register(r'ocupacion-lote', OcupacionLoteViewSet, basename='ocupacion-lote')


urlpatterns = router.urls
