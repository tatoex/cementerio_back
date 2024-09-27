from django.urls import path
from .views import ListTumbasView, DetailTumbaView, ListLotesView, DetailLoteView, ListDisponibleTumbasView, DetailDisponibleTumbaView

urlpatterns = [
    path('tumbas', ListTumbasView.as_view()),
    path('tumbas/<int:pk>/', DetailTumbaView.as_view()),
    path('lotes', ListLotesView.as_view()),
    path('lotes/<int:pk>/', DetailLoteView.as_view()),
    path('disponibleTumbas', ListDisponibleTumbasView.as_view()),
    path('disponibleTumbas/<int:pk>/', DetailTumbaView.as_view()),
]