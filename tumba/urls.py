from django.urls import path
from .views import ListTumbasView, DetailTumbaView

urlpatterns = [
    path('tumbas', ListTumbasView.as_view()),
    path('tumbas/<int:pk>/', DetailTumbaView.as_view()),
]