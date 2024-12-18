from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import CustomTokenObtainPairView
from .viewsets import UserProfileViewSet, GroupViewSet

# Configurar el router
router = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='profile')
router.register(r'group', GroupViewSet, basename='group')

# Rutas personalizadas
urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Combinar rutas del router con las rutas personalizadas
urlpatterns += router.urls