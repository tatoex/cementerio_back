# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import DifuntoSerializer, DeudoSerializer
from .models import Difunto, Deudo

# Create your views here.

class ListDifuntosView(ListAPIView, CreateAPIView):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset= Difunto.objects.all()
class DetailDifuntoView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=DifuntoSerializer
    #definir el queryset para traer los elementos
    queryset= Difunto.objects.all()

class ListDeudosView(ListAPIView, CreateAPIView):
    allowed_method = ['GET','POST']
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset= Deudo.objects.all()
class DetailDeudoView(RetrieveUpdateDestroyAPIView):
    allowed_method=['GET','PUT', 'DELETE']
    #para todos los metodos utilice el serializerclass
    serializer_class=DeudoSerializer
    #definir el queryset para traer los elementos
    queryset= Deudo.objects.all()

# clases APIView
# class ListDifuntosView(APIView):
    # def get(self, request):
    #     # traer los todos los elements de la clase tuba
    #     difuntos = Difunto.objects.all()
    #     # serializa los elements de difunto + de 1 (many=true)
    #     serializer = DifuntoSerializer(difuntos, many=True)
    #     return Response(serializer.data)
    # def post(self, request):
    #     # inserta la informacion que le pasan a traves del serializador
    #     serializer=DifuntoSerializer(data=request.data)
    #     # comprueba si el json es valido y si los captura y formate con raise_exception
    #     serializer.is_valid(raise_exception=True)
    #     #graba los parametros en la base de datos
    #     serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)
# class DetailDifuntoView(APIView):
    # def get(self,request,pk):
    #     try:
    #         difunto = Difunto.objects.get(id=pk)
    #     except Difunto.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     # serializa el elemento
    #     serializer = DifuntoSerializer(difunto)
    #     return Response(serializer.data)
    # def put(self,request,pk):
    #     try:
    #         difunto = Difunto.objects.get(id=pk)
    #     except Difunto.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = DifuntoSerializer(difunto, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # def delete(self,request,pk):
    #     try:
    #         difunto = Difunto.objects.get(id=pk)
    #     except Difunto.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     difunto.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

#decorador para hacer compatible a djrest sea compatible con esta vista
# @api_view(['GET','POST'])
# def list_difuntos(request):
#     #request nos permite difereciar el post y get
#     if request.method == 'GET':
#         # traer los todos los elements de la clase tuba
#         difuntos = Difunto.objects.all()
#         # serializa los elements de difunto + de 1 (many=true)
#         serializer = DifuntoSerializer(difuntos, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         # inserta la informacion que le pasan a traves del serializador
#         serializer=DifuntoSerializer(data=request.data)
#         # comprueba si el json es valido y si los captura y formate con raise_exception
#         serializer.is_valid(raise_exception=True)
#         #graba los parametros en la base de datos
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)
# @api_view(['GET','PUT', 'DELETE']) 
# def detail_difunto(request, pk):
#     # busca el id si no existe regresa el 404
#     try:
#         difunto = Difunto.objects.get(id=pk)
#     except Difunto.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         # serializa el elemento
#         serializer = DifuntoSerializer(difunto)
#         return Response(serializer.data)
#     # basicamente fucionamos el GET y POST
#     if request.method == 'PUT':
#         serializer = DifuntoSerializer(difunto, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     # en el metodo delete no usamos django rest
#     if request.method == 'DELETE':
#         difunto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)