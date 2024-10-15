from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import ListServiciosView, DetailServicioView, ListCeremoniasView, DetailCeremoniaView
from .viewsets import ServicioViewSet, CeremoniaViewSet, UserProfileViewSet, GroupViewSet

router=DefaultRouter()
router.register('servicio', ServicioViewSet)
router.register('ceremonia', CeremoniaViewSet)
router.register('profile', UserProfileViewSet)
router.register('group', GroupViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('servicios', ListServiciosView.as_view()),
#     path('servicios/<int:pk>/', DetailServicioView.as_view()),
#     path('ceremonias', ListCeremoniasView.as_view()),
#     path('ceremonias/<int:pk>/', DetailCeremoniaView.as_view()),
# ]