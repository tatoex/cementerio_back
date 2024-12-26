import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from obituarios.models import Obituario, Memoria, EtapasObituario
from django.utils.timezone import now

@pytest.mark.django_db
def test_list_obituarios(obituario):
    client = APIClient()
    response = client.get(reverse("obituario-list"))
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["obituary_detail"] == "Detalle del obituario"
    assert response.data["results"][0]["deceased"] == obituario.deceased.id

@pytest.mark.django_db
def test_create_obituario(difunto):
    client = APIClient()
    response = client.post(reverse("obituario-list"), {
        "obituary_detail": "Nuevo obituario",
        "deceased": difunto.id,
        "cementery": "Cementerio General",
        "place": "Capilla Principal",
        "name": "Juan Perez",
        "date_dead": now(),
        "date_born": now()
    })
    assert response.status_code == 201
    assert response.data["obituary_detail"] == "Nuevo obituario"
    assert response.data["deceased"] == difunto.id

@pytest.mark.django_db
def test_update_obituario(obituario):
    client = APIClient()
    response = client.put(reverse("obituario-detail", args=[obituario.id]), {
        "obituary_detail": "Actualizado",
        "deceased": obituario.deceased.id,
        "cementery": "Cementerio General",
        "place": "Nueva Capilla",
        "name": "Juan Perez Actualizado",
        "date_dead": now(),
        "date_born": now()
    })
    assert response.status_code == 200
    assert response.data["obituary_detail"] == "Actualizado"
    assert response.data["place"] == "Nueva Capilla"

@pytest.mark.django_db
def test_delete_obituario(obituario):
    client = APIClient()
    response = client.delete(reverse("obituario-detail", args=[obituario.id]))
    assert response.status_code == 204
    assert Obituario.objects.filter(id=obituario.id).count() == 0

@pytest.mark.django_db
def test_list_memorias(memoria):
    client = APIClient()
    response = client.get(reverse("memoria-list"))
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["names"] == "Carlos Sanchez"

@pytest.mark.django_db
def test_create_memoria(obituario):
    client = APIClient()
    response = client.post(reverse("memoria-list"), {
        "names": "Autor Test",
        "relationship": "Amigo",
        "text": "Un recuerdo inolvidable",
        "obituary": obituario.id
    })
    assert response.status_code == 201
    assert response.data["names"] == "Autor Test"
    assert response.data["obituary"] == obituario.id

@pytest.mark.django_db
def test_update_memoria(memoria):
    client = APIClient()
    response = client.put(reverse("memoria-detail", args=[memoria.id]), {
        "names": "Autor Actualizado",
        "relationship": "Familiar",
        "text": "Recuerdo actualizado",
        "obituary": memoria.obituary.id
    })
    assert response.status_code == 200
    assert response.data["names"] == "Autor Actualizado"
    assert response.data["text"] == "Recuerdo actualizado"

@pytest.mark.django_db
def test_delete_memoria(memoria):
    client = APIClient()
    response = client.delete(reverse("memoria-detail", args=[memoria.id]))
    assert response.status_code == 204
    assert Memoria.objects.filter(id=memoria.id).count() == 0

@pytest.mark.django_db
def test_list_etapas_obituario(etapa_obituario):
    client = APIClient()
    response = client.get(reverse("etapa-list"))
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["stage_ceremony"] == "Misa"

@pytest.mark.django_db
def test_create_etapa_obituario(obituario):
    client = APIClient()
    response = client.post(reverse("etapa-list"), {
        "stage_ceremony": "Velacion",
        "place": "Nueva Capilla",
        "obituary": obituario.id
    })
    assert response.status_code == 201
    assert response.data["stage_ceremony"] == "Velacion"
    assert response.data["obituary"] == obituario.id

@pytest.mark.django_db
def test_update_etapa_obituario(etapa_obituario):
    client = APIClient()
    response = client.put(reverse("etapa-detail", args=[etapa_obituario.id]), {
        "stage_ceremony": "Misa",  # Usa un valor válido
        "place": "Nueva Capilla",
        "obituary": etapa_obituario.obituary.id
    })
    assert response.status_code == 200
    assert response.data["place"] == "Nueva Capilla"
    assert response.data["stage_ceremony"] == "Misa"

@pytest.mark.django_db
def test_delete_etapa_obituario(etapa_obituario):
    client = APIClient()
    response = client.delete(reverse("etapa-detail", args=[etapa_obituario.id]))
    assert response.status_code == 204
    assert EtapasObituario.objects.filter(id=etapa_obituario.id).count() == 0
