from django.urls import reverse
from rest_framework.test import APIClient
from pytest import mark

@mark.django_db
def test_comparar_varias_versiones_success(servicio):
    client = APIClient()

    # Modificar el objeto para generar historial
    servicio.amount_paid = 150.00
    servicio.save()

    # Realizar la solicitud a la acción "comparar"
    url = reverse('servicio-history-list')
    response = client.get(f'{url}comparar/', {'object_id': servicio.id, 'attribute': 'amount_paid', 'limit': 5})
    
    assert response.status_code == 200
    assert 'cambios' in response.data


@mark.django_db
def test_historical_action_success(servicio):
    client = APIClient()

    # Modificar el objeto para generar historial
    servicio.amount_paid = 150.00
    servicio.save()

    # Realizar la solicitud a la acción "historical"
    url = reverse('servicio-history-historical')
    response = client.get(url, {'servicio_id': servicio.id, 'limit': 5})

    assert response.status_code == 200
    assert isinstance(response.data, list)  # El historial debería devolver una lista
    assert len(response.data) <= 5  # No debería exceder el límite de 5


@mark.django_db
def test_historical_action_no_id_provided():
    client = APIClient()

    # Realizar la solicitud sin un ID
    url = reverse('servicio-history-historical')
    response = client.get(url)
    
    assert response.status_code == 400
    assert 'error' in response.data


@mark.django_db
def test_restaurar_action_invalid_version():
    client = APIClient()

    # Realizar la solicitud con una versión inexistente
    url = reverse('servicio-history-restaurar')
    response = client.post(url, {'version_id': 9999})  # ID inexistente

    assert response.status_code == 404
    assert response.data.get("error") == "La versión especificada no existe"
