from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import ServicioReporteViewSet, ServicioViewSet, ServicioReadViewSet, TumbaEstadoViewSet

router=DefaultRouter()
router.register(r'servicio', ServicioViewSet, basename='servicio')
router.register(r'tumba-estado', TumbaEstadoViewSet, basename='tumba-estado')
router.register(r'servicioread', ServicioReadViewSet, basename='servicioread')
router.register(r'servicio-reporte', ServicioReporteViewSet, basename='servicio-reporte')

urlpatterns = router.urls

