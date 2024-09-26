from django.urls import path
from .views import list_difuntos, detail_difunto

urlpatterns = [
    path('difuntos', list_difuntos),
    path('difuntos/<int:pk>/', detail_difunto),
]