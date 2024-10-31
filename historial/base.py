from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import obtener_historial_limitado, compara_varias_versiones

class HistoricalActionMixin:
    """clase para manejar acciones: consultas, comparar y restaurar versiones """
    @action (methods=['GET'], detail=False, url_path='historial' )
    def historical(self, request):
        """
        Devuelve el historial del objeto segun su ID URL Parameters:
        - object_id: ID del objeto para obtener su historial.
        - limit: (opcional) Numero de verirsiones a mostrar (por defecto).
        """

        object_id=self.request.query_params.get(f'{self.model._meta.model_name.lower()}_id', None)
        limit=int(self.request.query_params.get('limit', 5))
        if not object_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            historial=obtener_historial_limitado(self.model, object_id, limit)
        except ValueError as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)
        #  serializar el historial para devolverlo como respuesta
        serializer=self.get_serializer(historial, many=True)
        return Response(serializer.data)
    
    @action (methods=['GET'], detail=False, url_path='comparar')
    def comparar_varias_versiones(self, request):
        """
        Compara varias versiones de un objeto en todos los atributos o en un atributo especifico
        URL Parameters:
        - object_id_ ID del objeto a comparar
        - attribute: (opcional) Atributoespecifico a comparar, usa 'all' para comparar todos los atributos.
        - limit: (opcional) Numero de versiones a considerar (por defecto 5).
        """
        object_id = self.request.query_params.get('object_id', None)
        attribute=self.request.query_params.get('attribute', 'all')
        limit = int(self.request.query_params.get('limit', 5))

        if not object_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # llama a la funcion para comparar varias versiones
            cambios=compara_varias_versiones(self.model, object_id, attribute, limit)
        except ValueError as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)

        return Response({"cambios":cambios})
    
    @action (methods=['POST'], detail=False, url_path='restaurar')
    def restaurar(self,request):
        """
        Restaura un objeto a una version anterior
        Body Parameters:
        - version_id: ID de la version historica que se desea restaurar
        """
        version_id=request.data.get('version_id',None)
        if not version_id:
            return Response({"error":"Debe proporcionar la ID del objeto"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # obtener la version historica
            version = self.model.history.get(history_id=version_id)
            # restauramos el objeto a la version anterior
            version.instance.save()
        except self.model.history.model.DoesNotExist:
            return Response({"error": "La versión especificada no existe"}, status=status.HTTP_404_NOT_FOUND)
    
        return Response({"mensaje": "Versión restaurada exitosamente"}, status=status.HTTP_200_OK)