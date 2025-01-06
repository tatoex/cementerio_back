import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_full_flow_obituario_creation(api_client, obituario, memoria, etapa_obituario):
    # Recuperar el Obituario
    response = api_client.get(reverse("obituario-detail", args=[obituario.id]))
    assert response.status_code == 200
    assert response.data["name"] == "Juan Perez"

    # Verifica la existencia de memorias asociadas utilizando el endpoint de Memoria
    response_memorias = api_client.get(reverse("memoria-list"), {"obituary": obituario.id})
    assert response_memorias.status_code == 200
    assert len(response_memorias.data["results"]) == 1
    assert response_memorias.data["results"][0]["names"] == "Carlos Sanchez"

    # Verifica la existencia de etapas asociadas utilizando el endpoint de EtapasObituario
    response_etapas = api_client.get(reverse("etapa-list"), {"obituary": obituario.id})
    assert response_etapas.status_code == 200
    assert len(response_etapas.data["results"]) == 1
    assert response_etapas.data["results"][0]["stage_ceremony"] == "Misa"
