from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from .serializers import ServicioSerializer, CeremoniaSerializer, UserProfileSerializer, GroupSerializer
from .models import Servicio, Ceremonia
from .filters import ServicioFilter, CeremoniaFilter
from .utils import sincronizar_disponibilidad_tumba

class ServicioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServicioFilter
    
    @action(methods=['POST'], detail=True, url_path='sincronizar-disponibilidad')
    def sincronizar_disponibilidad(self, request, pk=None):
        """accion para sincronizar las fechas de Disponibilidad de la tumba basado en funcion a servicio"""
        servicio=self.get_object()
        sincronizar_disponibilidad_tumba(servicio)
        return Response({'status':'Fechas sincronizadas :)'}, status=status.HTTP_200_OK)

class CeremoniaViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=CeremoniaSerializer
    #definir el queryset para traer los elementos
    queryset=Ceremonia.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CeremoniaFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()  # Obtiene el usuario autenticado
        serializer = self.get_serializer(user)  # Serializa el usuario
        return Response(serializer.data)  # Devuelve los datos serializados

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        group = self.get_object()
        return Response({
            'id': group.id,
            'name': group.name  # Devuelve el nombre del grupo (rol)
        })