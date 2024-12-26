import pytest
from tumba.models import Lote, Tumba
from difunto.models import Deudo, Difunto

@pytest.fixture
def lote():
    return Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

@pytest.fixture
def tumba(lote):
    return Tumba.objects.create(
        nicheNumber=1,
        nicheType="E",
        available=True,
        nameLote=lote
    )

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