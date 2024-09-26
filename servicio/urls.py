from django.urls import path
from .views import ListServiciosView, DetailServicioView

urlpatterns = [
    path('servicios', ListServiciosView.as_view()),
    path('servicios/<int:pk>/', DetailServicioView.as_view()),
]