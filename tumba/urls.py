from django.urls import path
from .views import list_tumbas, detail_tumba

urlpatterns = [
    path('tumbas', list_tumbas),
    path('tumbas/<int:pk>/', detail_tumba),
]