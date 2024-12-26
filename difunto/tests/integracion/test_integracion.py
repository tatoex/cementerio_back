import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, Lote

@pytest.mark.django_db
def test_difunto_deudo_relationship():
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
    assert difunto.deudo == deudo
    assert difunto.tumba == tumba

