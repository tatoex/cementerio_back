#from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ServicioSerializer, CeremoniaSerializer
from .models import Servicio, Ceremonia

# Create your views here.

class ListServiciosView(ListAPIView, CreateAPIView):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()
class DetailServicioView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=ServicioSerializer
    #definir el queryset para traer los elementos
    queryset=Servicio.objects.all()

class ListCeremoniasView(ListAPIView, CreateAPIView):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=CeremoniaSerializer
    #definir el queryset para traer los elementos
    queryset=Ceremonia.objects.all()
class DetailCeremoniaView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=CeremoniaSerializer
    #definir el queryset para traer los elementos
    queryset=Ceremonia.objects.all()

# clases APIView
# class ListServiciosView(APIView):
    # def get(self,request):
    #     # traer los todos los elements de la clase tuba
    #     servicios = Servicio.objects.all()
    #     # serializa los elements de servicio + de 1 (many=true)
    #     serializer = ServicioSerializer(servicios, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     # inserta la informacion que le pasan a traves del serializador
    #     serializer=ServicioSerializer(data=request.data)
    #     # comprueba si el json es valido y si los captura y formate con raise_exception
    #     serializer.is_valid(raise_exception=True)
    #     #graba los parametros en la base de datos
    #     serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)
# class DetailServicioView(APIView):
    # def get(self, request, pk):
    #     try:
    #         servicio = Servicio.objects.get(id=pk)
    #     except Servicio.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     # serializa el elemento
    #     serializer = ServicioSerializer(servicio)
    #     return Response(serializer.data)
    # def put(self, request, pk):
    #     try:
    #         servicio = Servicio.objects.get(id=pk)
    #     except Servicio.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = ServicioSerializer(servicio, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # def delete(self, request, pk):
    #     try:
    #         servicio = Servicio.objects.get(id=pk)
    #     except Servicio.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     servicio.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# decoradores   
#@api_view(['GET','PUT', 'DELETE']) 
#def detail_servicio(request, pk):
#    # busca el id si no existe regresa el 404
#    try:
#        servicio = Servicio.objects.get(id=pk)
#    except Servicio.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == 'GET':
#        # serializa el elemento
#        serializer = ServicioSerializer(servicio)
#        return Response(serializer.data)
#    # basicamente fucionamos el GET y POST
#    if request.method == 'PUT':
#        serializer = ServicioSerializer(servicio, data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data, status=status.HTTP_201_CREATED)
#    # en el metodo delete no usamos django rest
#    if request.method == 'DELETE':
#        servicio.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#decorador para hacer compatible a djrest sea compatible con esta vista
#@api_view(['GET','POST'])
#def list_servicios(request):
#    #request nos permite difereciar el post y get
#    if request.method == 'GET':
#        # traer los todos los elements de la clase tuba
#        servicios = Servicio.objects.all()
#        # serializa los elements de servicio + de 1 (many=true)
#        serializer = ServicioSerializer(servicios, many=True)
#        return Response(serializer.data)
#
#    if request.method == 'POST':
#        # inserta la informacion que le pasan a traves del serializador
#        serializer=ServicioSerializer(data=request.data)
#        # comprueba si el json es valido y si los captura y formate con raise_exception
#        serializer.is_valid(raise_exception=True)
#        #graba los parametros en la base de datos
#        serializer.save()
#        return Response(status=status.HTTP_201_CREATED)