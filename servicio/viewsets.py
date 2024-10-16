from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from .serializers import ServicioSerializer, UserProfileSerializer, GroupSerializer
from .models import Servicio
from .filters import ServicioFilter


class ServicioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServicioFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Queryset de todos los usuarios
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = request.user  # Obtiene el usuario autenticado
        serializer = self.get_serializer(user)  # Serializa el usuario
        return Response(serializer.data)  # Devuelve los datos serializados

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer  # Asegúrate de definir el serializer

    def retrieve(self, request, *args, **kwargs):
        group = self.get_object()  # Obtiene el grupo por ID
        return Response({
            'id': group.id,
            'name': group.name  # Devuelve el nombre del grupo (rol)
        })