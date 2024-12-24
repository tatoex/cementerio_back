import pytest
from .models import Lote, Tumba

@pytest.fixture
def lote():
    return Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )

@pytest.fixture
def tumba(lote):
    return Tumba.objects.create(
        nicheNumber=1,
        nicheType='T',
        available=True,
        nameLote=6000,
    )