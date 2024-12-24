import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from tumba.models import Tumba, Lote

@pytest.mark.django_db
def test_list_tumba():
    # Crear un Lote y Tumba de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )
    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)

    # Probar el endpoint de listar tumbas
    client = APIClient()
    response = client.get('/api/tumba/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1  # Confirmamos que haya una tumba creada
    assert response.data['results'][0]['nicheNumber'] == 1

@pytest.mark.django_db
def test_create_tumba():
    # Crear un lote de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )

    # Crear una tumba usando el endpoint
    client = APIClient()
    data = {
        'nicheNumber': 2,
        'nicheType': 'T',
        'available': True,
        'nameLote': lote.id
    }
    response = client.post('/api/tumba/', data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['nicheNumber'] == 2
    assert response.data['available'] is True

@pytest.mark.django_db
def test_update_tumba():
    # Crear un lote y tumba de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)

    # Actualizar la tumba
    client = APIClient()
    data = {
        'nicheNumber': 3,
        'nicheType': 'E',
        'available': False,
        'nameLote': lote.id  # Agregar el campo requerido
    }
    response = client.put(f'/api/tumba/{tumba.id}/', data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['nicheNumber'] == 3
    assert response.data['available'] is False

@pytest.mark.django_db
def test_delete_tumba():
    # Crear un lote y tumba de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)

    # Eliminar la tumba
    client = APIClient()
    response = client.delete(f'/api/tumba/{tumba.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Tumba.objects.filter(id=tumba.id).count() == 0

@pytest.mark.django_db
def test_set_on_available():
    # Crear un lote y tumba de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="T", available=False, nameLote=lote)

    # Usar la acción personalizada `set-on-available`
    client = APIClient()
    response = client.post(f'/api/tumba/{tumba.id}/set-on-available/')
    assert response.status_code == status.HTTP_200_OK
    tumba.refresh_from_db()
    assert tumba.available is True

@pytest.mark.django_db
def test_set_off_available():
    # Crear un lote y tumba de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)

    # Usar la acción personalizada `set-off-available`
    client = APIClient()
    response = client.post(f'/api/tumba/{tumba.id}/set-off-available/')
    assert response.status_code == status.HTTP_200_OK
    tumba.refresh_from_db()
    assert tumba.available is False

@pytest.mark.django_db
def test_list_lote():
    # Crear un lote de prueba
    Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=20)

    # Probar el endpoint de listar lotes
    client = APIClient()
    response = client.get('/api/lote/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1  # Confirmamos que haya un lote creado
    assert response.data['results'][0]['blockName'] == 1

@pytest.mark.django_db
def test_create_lote():
    # Crear un lote usando el endpoint
    client = APIClient()
    data = {
        'blockName': 2,
        'typeblock': "B",
        'numbersblock': 15,
        'filas': 5,
        'columnas': 3,
        'limite': 30
    }
    response = client.post('/api/lote/', data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['blockName'] == 2
    assert response.data['limite'] == 30

@pytest.mark.django_db
def test_update_lote():
    # Crear un lote de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )

    # Actualizar el lote
    client = APIClient()
    data = {
        'blockName': 2,
        'typeblock': "B",
        'numbersblock': 15,
        'filas': 6,
        'columnas': 3,
        'limite': 25
    }
    response = client.put(f'/api/lote/{lote.id}/', data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['blockName'] == 2
    assert response.data['typeblock'] == "B"
    assert response.data['limite'] == 25

@pytest.mark.django_db
def test_delete_lote():
    # Crear un lote de prueba
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )

    # Eliminar el lote
    client = APIClient()
    response = client.delete(f'/api/lote/{lote.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Lote.objects.filter(id=lote.id).count() == 0

@pytest.mark.django_db
def test_tumba_pagination():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=30)  # Límite ajustado
    for i in range(25):
        Tumba.objects.create(nicheNumber=i + 1, nicheType="T", available=True, nameLote=lote)

    # Verificar la paginación
    url = reverse("tumba-estado-list")  # Asegúrate de que la URL del endpoint sea correcta
    response = APIClient().get(url, {"page_size": 10})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 10  # Comprobar que hay 10 elementos en la primera página
    assert response.data["count"] == 25  # Verificar el total de elementos


@pytest.mark.django_db
def test_create_tumba_exceed_lote_limit():
    # Crear un lote con un límite de 2 tumbas
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=2)
    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    Tumba.objects.create(nicheNumber=2, nicheType="T", available=True, nameLote=lote)

    # Intentar crear otra tumba mediante la API
    client = APIClient()
    data = {
        'nicheNumber': 3,
        'nicheType': 'T',
        'available': True,
        'nameLote': lote.id
    }
    response = client.post('/api/tumba/', data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['error'] == 'No se pueden agregar más tumbas, se ha alcanzado el límite del lote.'

@pytest.mark.django_db
def test_update_nonexistent_tumba():
    client = APIClient()
    data = {'nicheNumber': 1, 'nicheType': 'T', 'available': True}
    response = client.put('/api/tumba/9999/', data)
    assert response.status_code == status.HTTP_404_NOT_FOUND