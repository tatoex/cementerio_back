import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from difunto.models import Difunto
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, Lote


@pytest.mark.django_db
def test_list_difuntos(deudo, tumba):
    client = APIClient()
    Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    response = client.get(reverse("difunto-list"))
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["names"] == "Juan"
    assert response.data["results"][0]["deudo"] == deudo.id


@pytest.mark.django_db
def test_create_difunto(deudo, tumba):
    client = APIClient()
    response = client.post(reverse("difunto-list"), {
        "names": "Juan",
        "last_names": "Pérez",
        "idNumber": "0987654321",
        "requestNumber": "REQ001",
        "tumba": tumba.id,
        "deudo": deudo.id,
        "description": "N/A"
    })
    assert response.status_code == 201
    assert response.data["names"] == "Juan"
    assert response.data["deudo"] == deudo.id


@pytest.mark.django_db
def test_update_difunto(deudo, tumba):
    client = APIClient()
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    response = client.put(reverse("difunto-detail", args=[difunto.id]), {
        "names": "Juan",
        "last_names": "López",
        "idNumber": "0987654321",
        "requestNumber": "REQ002",
        "tumba": tumba.id,
        "deudo": deudo.id,
        "description": "Actualizado"
    })
    assert response.status_code == 200
    assert response.data["last_names"] == "López"
    assert response.data["description"] == "Actualizado"


@pytest.mark.django_db
def test_delete_difunto(deudo, tumba):
    client = APIClient()
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    response = client.delete(reverse("difunto-detail", args=[difunto.id]))
    assert response.status_code == 204
    # Verifica que el objeto ya no existe
    assert Difunto.objects.filter(id=difunto.id).count() == 0

@pytest.mark.django_db
def test_list_deudos():
    client = APIClient()
    response = client.get(reverse("deudo-list"))
    assert response.status_code == 200
    assert "results" in response.data


@pytest.mark.django_db
def test_create_deudo():
    client = APIClient()
    response = client.post(reverse("deudo-list"), {
        "names": "Jane",
        "last_names": "Smith",
        "idNumber": "0987654321",
        "phoneNumber": "0987654322",
        "email": "jane.smith@example.com",
        "address": "Quito",
        "tipo": "Conocido"
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_deudo(deudo):
    client = APIClient()
    response = client.put(reverse("deudo-detail", args=[deudo.id]), {
        "names": "Jane",
        "last_names": "Doe",
        "idNumber": "1234567890",
        "phoneNumber": "0987654321",
        "email": "jane.doe@example.com",
        "address": "Guayaquil",
        "tipo": "Familiar"
    })
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_deudo(deudo):
    client = APIClient()
    response = client.delete(reverse("deudo-detail", args=[deudo.id]))
    assert response.status_code == 204


@pytest.mark.django_db
def test_filter_deudos_by_tipo(deudo):
    client = APIClient()
    response = client.get(reverse("deudo-list") + "?tipo=Familiar")
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["tipo"] == "Familiar"


@pytest.mark.django_db
def test_filter_difuntos_by_request_number(deudo, tumba):
    client = APIClient()
    Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    response = client.get(reverse("difunto-list") + "?requestNumber=REQ001")
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["requestNumber"] == "REQ001"
