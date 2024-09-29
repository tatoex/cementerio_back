from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import consultar_historial, obtener_difernecia, restaurar_version

class HistoricalQuerySetMixin:
    """clase para manejar la obtencionde datos del historial de cualquier modelo con filtros"""
    def get_queryset(self):
        """Retorna el historial filtrada si se proporciona"""
        # Id
        object_id=self.request.query_params.get(f'{self.model_name.lower()}_id', None)
        if object_id:
            queryset=queryset.filter(id=object_id).order_by('-history_date')

        # Fechas
        start_date = self.request.query_params.get('stat_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date:
            queryset=queryset.filter(histoy_date__gte=start_date)
        if end_date:
            queryset=queryset.filter(histoy_date__lte=end_date)
        
        # Tipo accio
        history_type=self.request.query_params.get('history_type', None)
        if history_type:
            queryset=queryset.filter(history_type=history_type)
        
        # Usuario
        user_id=self.request.query_params.get('user_id', None)
        if user_id:
            queryset=queryset.filter(history_user_id=user_id)
        return queryset

class HistoricalActionMixin:
    """clase para manejar acciones: consultas, comparar y restaurar versiones """
    @action (detail=False, methods=['get'])
    def historical(self, request):
        """devuelve el historial del objeto"""

        object_id=self.request.query_params.get(f'{self.model_name.lower()}_id')
        if not object_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        historial=consultar_historial(self.model,object_id)
        serializer=self.get_serializer(historial, many=True)
        return Response(serializer.data)
    
    @action (detail=False, methods=['get'])
    def comparar(self, request):
        """compara dos versiones del historial"""
        version1_id=request.query_params.get('version1_id')
        version2_id=request.query_params.get('version2_id')

        if not version1_id or not version2_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        
        version1=self.model.history.get(histort_id=version1_id)
        version2=self.model.history.get(histort_id=version2_id)

        diferencias=obtener_difernecia(version1, version2)
        return Response({"diferencias":diferencias})
    
    @action (detail=False, methods=['post'])
    def restaurar(self,request):
        """Restaura yb objeto a una version anterior"""
        version_id=request.data.get(version_id)
        if not version_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        version=self.model.histry.get(hitory_id=version_id)
        restaurar_version(version)
        return Response({"mensaje":"Version restaurada exitosamente"})