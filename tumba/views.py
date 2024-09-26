from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import LoteSerializer, TumbaSerializer, DisponibleTumbaSerializer
from .models import Lote, Tumba, DisponibleTumba

# Create your views here.

#decorador para hacer compatible a djrest sea compatible con esta vista
@api_view(['GET','POST'])
def list_tumbas(request):
    #request nos permite difereciar el post y get
    if request.method == 'GET':
        # traer los todos los elements de la clase tuba
        tumbas = Tumba.objects.all()
        # serializa los elements de tumba + de 1 (many=true)
        serializer = TumbaSerializer(tumbas, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        # inserta la informacion que le pasan a traves del serializador
        serializer=TumbaSerializer(data=request.data)
        # comprueba si el json es valido y si los captura y formate con raise_exception
        serializer.is_valid(raise_exception=True)
        #graba los parametros en la base de datos
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE']) 
def detail_tumba(request, pk):
    # busca el id si no existe regresa el 404
    try:
        tumba = Tumba.objects.get(id=pk)
    except Tumba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # serializa el elemento
        serializer = TumbaSerializer(tumba)
        return Response(serializer.data)
    # basicamente fucionamos el GET y POST
    if request.method == 'PUT':
        serializer = TumbaSerializer(tumba, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # en el metodo delete no usamos django rest
    if request.method == 'DELETE':
        tumba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)