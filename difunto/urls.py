from django.urls import path
from .views import ListDifuntosView, DetailDifuntoView, ListDeudosView, DetailDeudoView

urlpatterns = [
    path('difuntos', ListDifuntosView.as_view()),
    path('difuntos/<int:pk>/', DetailDifuntoView.as_view()),
    path('deudos', ListDeudosView.as_view()),
    path('deudos/<int:pk>/', DetailDeudoView.as_view()),
    
]