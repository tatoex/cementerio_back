from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import ListDifuntosView, DetailDifuntoView, ListDeudosView, DetailDeudoView
from.viewsets import DifuntoViewSet, DeudoViewSet, DifuntoReadViewSet, DeudoReadViewSet

router=DefaultRouter()
router.register(r'difunto', DifuntoViewSet, basename='difunto')
router.register(r'deudo', DeudoViewSet, basename='deudo')
router.register(r'difuntoread', DifuntoReadViewSet, basename='difuntoread')
router.register(r'deudoread', DeudoReadViewSet, basename='deudoread')

urlpatterns = router.urls

# urlpatterns = [
#     path('difuntos', ListDifuntosView.as_view()),
#     path('difuntos/<int:pk>/', DetailDifuntoView.as_view()),
#     path('deudos', ListDeudosView.as_view()),
#     path('deudos/<int:pk>/', DetailDeudoView.as_view()),
    
# ]