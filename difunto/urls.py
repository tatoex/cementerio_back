from django.urls import path
from .views import ListDifuntosView, DetailDifuntoView

urlpatterns = [
    path('difuntos', ListDifuntosView.as_view()),
    path('difuntos/<int:pk>/', DetailDifuntoView.as_view()),
]