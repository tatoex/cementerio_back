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
# from .views import ListTumbasView, DetailTumbaView, ListLotesView, DetailLoteView, ListDisponibleTumbasView, DetailDisponibleTumbaView

# urlpatterns = [
#     path('tumbas', ListTumbasView.as_view()),
#     path('tumbas/<int:pk>/', DetailTumbaView.as_view()),
#     path('lotes', ListLotesView.as_view()),
#     path('lotes/<int:pk>/', DetailLoteView.as_view()),
#     path('disponibleTumbas', ListDisponibleTumbasView.as_view()),
#     path('disponibleTumbas/<int:pk>/', DetailTumbaView.as_view()),
# ]