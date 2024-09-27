from django.urls import path
from .views import ListServiciosView, DetailServicioView, ListCeremoniasView, DetailCeremoniaView

urlpatterns = [
    path('servicios', ListServiciosView.as_view()),
    path('servicios/<int:pk>/', DetailServicioView.as_view()),
    path('ceremonias', ListCeremoniasView.as_view()),
    path('ceremonias/<int:pk>/', DetailCeremoniaView.as_view()),
]