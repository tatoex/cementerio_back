from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import ListTumbasView, DetailTumbaView, ListLotesView, DetailLoteView, ListDisponibleTumbasView, DetailDisponibleTumbaView
from .viewsets import TumbaViewSet, LoteViewSet

router=DefaultRouter()
router.register(r'tumba', TumbaViewSet)
router.register(r'lote', LoteViewSet)


urlpatterns = router.urls
# urlpatterns = [
#     path('tumbas', ListTumbasView.as_view()),
#     path('tumbas/<int:pk>/', DetailTumbaView.as_view()),
#     path('lotes', ListLotesView.as_view()),
#     path('lotes/<int:pk>/', DetailLoteView.as_view()),
#     path('disponibleTumbas', ListDisponibleTumbasView.as_view()),
#     path('disponibleTumbas/<int:pk>/', DetailTumbaView.as_view()),
# ]