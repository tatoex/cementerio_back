import pytest
from django.urls import reverse
from rest_framework import status
from servicio.models import Servicio
from tumba.models import Tumba, Lote
from difunto.models import Difunto, Deudo
from decimal import Decimal
from django.utils.timezone import now as timezone_now
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def lote():
    return Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

@pytest.fixture
def tumba(lote):
    return Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)

@pytest.fixture
def deudo():
    return Deudo.objects.create(
        names="John",
        last_names="Doe",
        idNumber="1234567890",
        phoneNumber="0987654321",
        email="john.doe@example.com",
        address="Quito",
        tipo="Familiar"
    )

@pytest.fixture
def difunto(tumba, deudo):
    return Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        deudo=deudo,
        tumba=tumba
    )

@pytest.fixture
def servicio(tumba, difunto):
    return Servicio.objects.create(
        ceremony="Inhumacion",
        is_paid=False,
        amount_paid=Decimal("100.50"),
        numberTomb=tumba,
        deceased=difunto
    )

@pytest.mark.django_db
def test_list_servicios_integration(api_client, servicio):
    url = reverse('servicio-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) > 0
    assert any(item['ceremony'] == "Inhumacion" for item in response.data['results'])

@pytest.mark.django_db
def test_create_servicio_integration(api_client, tumba, difunto):
    url = reverse('servicio-list')
    data = {
        "startDate": timezone_now().isoformat(),
        "ceremony": "Cremacion",
        "numberTomb": tumba.id,
        "deceased": difunto.id,
        "amount_paid": "200.00"
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Servicio.objects.filter(ceremony="Cremacion", deceased=difunto).exists()

@pytest.mark.django_db
def test_update_servicio_integration(api_client, servicio):
    url = reverse('servicio-detail', args=[servicio.id])
    data = {
        "is_paid": True
    }
    response = api_client.patch(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    servicio.refresh_from_db()
    assert servicio.is_paid is True

@pytest.mark.django_db
def test_delete_servicio_integration(api_client, servicio):
    url = reverse('servicio-detail', args=[servicio.id])
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Servicio.objects.filter(id=servicio.id).exists()

@pytest.mark.django_db
def test_filter_servicio_by_ceremony(api_client, servicio):
    url = reverse('servicio-list') + f'?ceremony={servicio.ceremony}'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) > 0
    assert all(item['ceremony'] == servicio.ceremony for item in response.data['results'])

@pytest.mark.django_db
def test_difuntos_por_tipo_servicio_integration(api_client, servicio):
    url = reverse('servicio-difuntos-por-tipo-servicio')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert any(item['ceremony'] == servicio.ceremony for item in response.data)
