from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import consultar_historial, obtener_difernecia, restaurar_version

class HistoricalQuerySetMixin:
    """clase para manejar la obtencionde datos del historial de cualquier modelo con filtros"""
    def get_queryset(self):
        """Retorna el historial filtrada si se proporciona"""
        queryset=self.model.history.all()
        # Id
        entity_id=self.request.query_params.get(f'{self.model._meta.model_name.lower()}_id', None)
        # Fechas
        start_date = self.request.query_params.get('stat_date', None)
        end_date = self.request.query_params.get('end_date', None)
        # Tipo accio
        history_type=self.request.query_params.get('history_type', None)
        # Usuario
        user_id=self.request.query_params.get('user_id', None)

        if entity_id:
            queryset=queryset.filter(id=entity_id).order_by('-history_date')
        if start_date:
            queryset=queryset.filter(histoy_date__gte=start_date)
        if end_date:
            queryset=queryset.filter(histoy_date__lte=end_date)
        if history_type:
            queryset=queryset.filter(history_type=history_type)
        if user_id:
            queryset=queryset.filter(history_user_id=user_id)
        return queryset

class HistoricalActionMixin:
    """clase para manejar acciones: consultas, comparar y restaurar versiones """
    @action (methods=['GET'], detail=False, url_path='historial' )
    def historical(self, request):
        """devuelve el historial del objeto"""

        object_id=self.request.query_params.get(f'{self.model._meta.model_name.lower()}_id', None)
        if not object_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        historial=consultar_historial(self.model,object_id)
        serializer=self.get_serializer(historial, many=True)
        return Response(serializer.data)
    
    @action (methods=['GET'], detail=False, url_path='comparar')
    def comparar(self, request):
        """compara dos versiones del historial"""
        version1_id=request.query_params.get('version1_id')
        version2_id=request.query_params.get('version2_id')

        if not version1_id or not version2_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        
        if version1_id==version2_id:
            return Response({"error":"No se puede comparar la misma version. Proporcione versiones diferentes"},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            version1=self.model.history.get(history_id=version1_id)
            version2=self.model.history.get(history_id=version2_id)
        except self.model.history.model.DoesNotExist:
            return Response({"error":"Una de las versiones no existe"},status=status.HTTP_404_NOT_FOUND)
        
        diferencias=obtener_difernecia(version1, version2)
        return Response({"diferencias":diferencias})
    
    @action (methods=['GET'], detail=False, url_path='restaurar')
    def restaurar(self,request):
        """Restaura yb objeto a una version anterior"""
        version_id=request.data.get('version_id')
        if not version_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        version=self.model.histry.get(hitory_id=version_id)
        restaurar_version(version)
        return Response({"mensaje":"Version restaurada exitosamente"})