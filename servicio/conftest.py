import pytest
from django.utils.timezone import now
from django.utils.timezone import now as timezone_now
from tumba.models import Tumba, Lote
from difunto.models import Difunto, Deudo
from decimal import Decimal
from servicio.models import Servicio
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

# Fixture para crear un objeto deudo
@pytest.fixture
def deudo():
    """
    Crea y devuelve un objeto Deudo para ser utilizado en las pruebas.
    """
    return Deudo.objects.create(
        names="John",
        last_names="Doe",
        idNumber="1234567890",
        phoneNumber="0987654321",
        email="john.doe@example.com",
        address="Quito",
        tipo="Familiar"
    )

# Fixture para crear un objeto lote
@pytest.fixture
def lote():
    """
    Crea y devuelve un objeto Lote con un blockName válido.
    """
    return Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

# Fixture para crear un objeto tumba asociado a un lote
@pytest.fixture
def tumba(lote):
    """
    Crea y devuelve un objeto Tumba asociado al lote proporcionado.
    """
    return Tumba.objects.create(
        id=6000,
        nicheNumber=0,
        nicheType="T",
        available=True,
        nameLote=lote
    )

# Fixture para crear un objeto difunto asociado a una tumba y un deudo
@pytest.fixture
def difunto(tumba, deudo):
    """
    Crea y devuelve un objeto Difunto asociado a una tumba y un deudo.
    """
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
        startDate=timezone_now(),
        ceremony="Inhumacion",
        is_paid=False,
        amount_paid=Decimal("100.50"),
        numberTomb=tumba,
        deceased=difunto
    )
