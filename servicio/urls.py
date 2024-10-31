from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import ListServiciosView, DetailServicioView, ListCeremoniasView, DetailCeremoniaView
from .viewsets import ServicioViewSet, ServicioReadViewSet, UserProfileViewSet, GroupViewSet

router=DefaultRouter()
router.register(r'servicio', ServicioViewSet, basename='servicio')
router.register(r'servicioread', ServicioReadViewSet, basename='servicioread')
router.register(r'profile', UserProfileViewSet, basename='profile')
router.register(r'group', GroupViewSet, basename='group')

urlpatterns = router.urls

# urlpatterns = [
#     path('servicios', ListServiciosView.as_view()),
#     path('servicios/<int:pk>/', DetailServicioView.as_view()),
#     path('ceremonias', ListCeremoniasView.as_view()),
#     path('ceremonias/<int:pk>/', DetailCeremoniaView.as_view()),
# ]