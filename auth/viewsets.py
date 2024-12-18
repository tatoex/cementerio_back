from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cemeteryapp.permissions import IsInGroup
from .serializers import UserProfileSerializer, GroupSerializer

class SecretariaViewSet(ViewSet):
    """
    ViewSet accesible solo para usuarios del grupo 'Secretaria'.
    """
    permission_classes = [IsAuthenticated, IsInGroup]
    required_group = 'Secretaria'

    def list(self, request):
        """
        Endpoint para listar recursos específicos de secretaria.
        """
        return Response({"message": "Acceso permitido a Secretaría", "user": request.user.username})

class AdminViewSet(ViewSet):
    """
    ViewSet accesible solo para usuarios del grupo 'Administrador'.
    """
    permission_classes = [IsAuthenticated, IsInGroup]
    required_group = 'Administrador'

    def list(self, request):
        """
        Endpoint para listar recursos específicos del administrador.
        """
        return Response({"message": "Acceso permitido a Administrador", "user": request.user.username})
    
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
