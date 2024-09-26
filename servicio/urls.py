from django.urls import path
from .views import list_servicios, detail_servicio

urlpatterns = [
    path('servicios', list_servicios),
    path('servicios/<int:pk>/', detail_servicio),
]