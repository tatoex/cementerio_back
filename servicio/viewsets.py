from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, status
from django.db.models import Count
from .serializers import ServicioSerializer, UserProfileSerializer, GroupSerializer, TumbaEstadoSerializer
from .models import Servicio
from tumba.models import Tumba
from .filters import ServicioFilter
from tumba.filters import TumbaFilter
from django.db.models import Count, Q
from .serializers import ServicioReporteSerializer

class PagionacionServicio(PageNumberPagination):
    page_size = 17
    page_size_query_param = 'page_size'
    max_page_size = 105


class DynamicTumbaPagination(PageNumberPagination):
    page_size = 17  # Tamaño de página predeterminado si no hay filtro
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_page_size(self, request):
        # Obtén el parámetro `nameLote` desde el request como ID de Lote
        name_lote_id = request.query_params.get('nameLote')
        
        if name_lote_id:
            try:
                # Filtra las tumbas según el ID de `nameLote`
                total_tumbas = Tumba.objects.filter(nameLote_id=name_lote_id).count()
                return total_tumbas or self.page_size  # Usa el total de tumbas o el `page_size` predeterminado
            except ValueError:
                # Maneja posibles errores en caso de que `nameLote` no sea un entero válido
                return self.page_size

        return super().get_page_size(request)  # Usa el tamaño de página predeterminado si no hay `nameLote`

class ServicioViewSet(viewsets.ModelViewSet):
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServicioFilter
    pagination_class = PagionacionServicio

    @action(detail=False, methods=['get'], url_path='difuntos-por-tipo-servicio')
    def difuntos_por_tipo_servicio(self, request):
        # Realiza la agregación para contar difuntos por tipo de servicio
        data = (
            self.get_queryset()
            .values('ceremony')
            .annotate(difunto_count=Count('deceased'))
            .order_by('ceremony')
        )
        return Response(data)
    @action(methods=['POST'], detail=True, url_path='set-on-paid')
    def set_on_paid(self, request, pk):
        servicio = self.get_object()
        servicio.is_paid=True
        servicio.save()
        return Response ({"status":"Esta cancelado"})
    @action(methods=['POST'], detail=True, url_path='set-off-paid')
    def set_off_paid(self, request, pk):
        servicio = self.get_object()
        servicio.is_paid=False
        servicio.save()
        return Response ({"status":"No esta cancelado"})
    
class TumbaEstadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tumba.objects.all().order_by('nicheNumber') 
    serializer_class = TumbaEstadoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TumbaFilter
    pagination_class = DynamicTumbaPagination

class ServicioReadViewSet(viewsets.ReadOnlyModelViewSet):
    # Configuramos el serializer para todos los métodos
    serializer_class = ServicioSerializer
    # Definimos el queryset para traer todos los elementos
    queryset = Servicio.objects.all().order_by('numberTomb')
    # Agregamos el backend de filtros y el filtro correspondiente
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServicioFilter
    # Agregamos la configuración de paginación personalizada

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

    

class ServicioReporteViewSet(viewsets.ViewSet):
    def list(self, request):
        # Agrupar los servicios por tipo de ceremonia y estado
        data = Servicio.objects.values('ceremony').annotate(
            activos=Count('id', filter=Q(endDate__isnull=True, is_paid=True)),
            completados=Count('id', filter=Q(endDate__isnull=False, is_paid=True)),
            pendiente_pago=Count('id', filter=Q(is_paid=False))
        )

        return Response(data)