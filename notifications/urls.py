from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NotificationViewSet

# Crear un router para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'notificacion', NotificationViewSet, basename='notificacion')

urlpatterns = router.urls