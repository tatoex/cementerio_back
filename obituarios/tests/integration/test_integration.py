import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils.timezone import now
from tumba.models import Lote, Tumba
from difunto.models import Deudo, Difunto
from obituarios.models import Obituario, Memoria, EtapasObituario

@pytest.mark.django_db
def test_full_flow_obituario_creation():
    client = APIClient()

    # Crear los datos iniciales
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John",
        last_names="Doe",
        idNumber="1234567890",
        phoneNumber="0987654321",
        email="john.doe@example.com",
        address="Quito",
        tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    obituario = Obituario.objects.create(
        obituary_detail="Detalle del obituario",
        cementery="Cementerio Central",
        place="Capilla Principal",
        name="Juan Pérez",
        deceased=difunto,
        date_dead=now(),
        date_born=now()
    )
    memoria = Memoria.objects.create(
        names="Carlos Sanchez",
        relationship="Amigo",
        text="Un hermoso recuerdo para siempre",
        obituary=obituario
    )
    etapa = EtapasObituario.objects.create(
        stage_ceremony="Misa",
        place="Capilla Principal",
        obituary=obituario
    )

    # Recuperar el Obituario
    response = client.get(reverse("obituario-detail", args=[obituario.id]))
    assert response.status_code == 200
    assert response.data["name"] == "Juan Pérez"

    # Verifica la existencia de memorias asociadas utilizando el endpoint de Memoria
    response_memorias = client.get(reverse("memoria-list"), {"obituary": obituario.id})
    assert response_memorias.status_code == 200
    assert len(response_memorias.data["results"]) == 1
    assert response_memorias.data["results"][0]["names"] == "Carlos Sanchez"

    # Verifica la existencia de etapas asociadas utilizando el endpoint de EtapasObituario
    response_etapas = client.get(reverse("etapa-list"), {"obituary": obituario.id})
    assert response_etapas.status_code == 200
    assert len(response_etapas.data["results"]) == 1
    assert response_etapas.data["results"][0]["stage_ceremony"] == "Misa"
