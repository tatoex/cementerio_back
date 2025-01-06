import pytest
from datetime import timedelta
from django.utils.timezone import now
from decimal import Decimal
from difunto.models import Deudo, Difunto
from tumba.models import Lote, Tumba
from servicio.models import Servicio
from obituarios.models import Obituario


@pytest.fixture
def lote():
    return Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)


@pytest.fixture
def tumba(lote):
    return Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)


@pytest.fixture
def deudo():
    return Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )


@pytest.fixture
def difunto(deudo, tumba):
    return Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ001", deudo=deudo, tumba=tumba
    )


@pytest.fixture
def servicio(difunto, tumba):
    return Servicio.objects.create(
        startDate=now(),
        endDate=now() + timedelta(days=7),
        ceremony="Inhumacion",
        is_paid=True,
        amount_paid=Decimal("100.00"),
        payment_date=now(),
        description="Servicio inicial",
        numberTomb=tumba,
        deceased=difunto
    )


@pytest.fixture
def obituario(difunto):
    return Obituario.objects.create(
        obituary_detail="Mensaje de prueba para el obituario.",
        cementery="Cementerio General",
        place="Capilla A",
        name="María Gómez",
        deceased=difunto,
        date_dead=now(),
        date_born=now() - timedelta(days=365 * 50)  # Simulando que nació hace 50 años
    )