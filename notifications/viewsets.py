from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Notification
from .serializers import NotificationSerializer
from .filters import NotificationFilter


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # permission_classes = [AllowAny]  # Permite que personas no autenticadas accedan a este ViewSet
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotificationFilter

    @action(detail=True, methods=['PATCH'], url_path='mark-as-attended')
    def mark_as_attended(self, request, pk=None):

            notification = self.get_object()
            notification.is_attended = True
            notification.save()
            return Response({"message": "Notificación marcada como atendida."}, status=200)

    @action(detail=True, methods=['PATCH'], url_path='mark-as-attended-off')
    def mark_as_attended_off(self, request, pk=None):
        try:
            notification = self.get_object()
            notification.is_attended = False
            notification.save()
            return Response({"message": "Notificación marcada como atendida."}, status=200)
        except Notification.DoesNotExist:
            return Response({"error": "Notificación no encontrada."}, status=404)
        # def list(self, request, *args, **kwargs):
    #     """
    #     Devuelve solo las notificaciones que no han sido atendidas.
    #     """
    #     notifications = Notification.objects.filter(is_attended=False)
    #     serializer = self.get_serializer(notifications, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     """
    #     Permite crear una nueva notificación sin necesidad de autenticación.
    #     """
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=201)