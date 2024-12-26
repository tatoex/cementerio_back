import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.core.exceptions import ValidationError
from rest_framework import status
from django.utils.timezone import now as timezone_now
from servicio.models import Servicio
from tumba.models import Tumba, Lote
from difunto.models import Difunto, Deudo
from datetime import datetime
from decimal import Decimal


@pytest.mark.django_db
def test_list_servicios(api_client, servicio):
    """
    Prueba que el endpoint para listar servicios funcione correctamente.
    Valida que el servicio creado esté en la respuesta.
    """
    url = reverse('servicio-list')  # Nombre del endpoint para listar servicios
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['ceremony'] == "Inhumacion"

@pytest.mark.django_db
def test_create_servicio(client, tumba, difunto):
    """
    Prueba que el endpoint para crear un servicio permita la creación exitosa.
    """
    response = client.post('/api/servicio/', {
        "ceremony": "Inhumacion",
        "numberTomb": tumba.id,
        "deceased": difunto.id
    })

    assert response.status_code == 201

@pytest.mark.django_db
def test_set_on_paid(api_client, servicio):
    """
    Prueba que el endpoint para marcar un servicio como pagado funcione correctamente.
    """
    url = reverse('servicio-set-on-paid', args=[servicio.id])
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    servicio.refresh_from_db()
    assert servicio.is_paid is True
    assert response.data['status'] == "Esta cancelado"

@pytest.mark.django_db
def test_set_off_paid(api_client, servicio):
    """
    Prueba que el endpoint para marcar un servicio como no pagado funcione correctamente.
    """
    url = reverse('servicio-set-off-paid', args=[servicio.id])
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    servicio.refresh_from_db()
    assert servicio.is_paid is False
    assert response.data['status'] == "No esta cancelado"

@pytest.mark.django_db
def test_difuntos_por_tipo_servicio(api_client, servicio):
    """
    Prueba que el endpoint de agregación devuelva el conteo correcto de difuntos por tipo de servicio.
    """
    url = reverse('servicio-difuntos-por-tipo-servicio')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['ceremony'] == "Inhumacion"
    assert response.data[0]['difunto_count'] == 1

@pytest.mark.django_db
def test_lote_block_name_validation():
    """
    Prueba que el campo blockName del modelo Lote valide correctamente los valores permitidos.
    """
    # Caso: Valor mayor al permitido
    with pytest.raises(ValidationError, match="Ensure this value is less than or equal to 12."):
        Lote.objects.create(blockName=13, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

    # Caso: Valor menor al permitido
    with pytest.raises(ValidationError, match="Ensure this value is greater than or equal to 1."):
        Lote.objects.create(blockName=0, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)