import pytest
from rest_framework.test import APIClient
from datetime import timedelta
from django.utils.timezone import now
from decimal import Decimal
from difunto.models import Deudo, Difunto
from tumba.models import Lote, Tumba
from servicio.models import Servicio
from obituarios.models import Obituario

@pytest.mark.django_db
def test_full_flow_obituario_creation():
    client = APIClient()

    # Crear los datos iniciales
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ001", deudo=deudo, tumba=tumba
    )
    servicio = Servicio.objects.create(
        startDate=now(),
        endDate=now() + timedelta(days=7),
        ceremony="Inhumacion",
        is_paid=True,
        amount_paid=Decimal("100.00"),
        payment_date=now(),
        description="Servicio de prueba",
        numberTomb=tumba,
        deceased=difunto
    )
    
    # Crear un obituario
    obituario = Obituario.objects.create(
        obituary_detail="Mensaje de prueba para el obituario.",
        cementery="Cementerio General",
        place="Capilla A",
        name="María Gómez",
        deceased=difunto,
        date_dead=now(),
        date_born=now() - timedelta(days=365 * 50)  # Simulando que nació hace 50 años
    )

    # Verificar que el obituario se creó correctamente
    assert obituario.deceased == difunto
    assert obituario.name == "María Gómez"
    assert obituario.cementery == "Cementerio General"
    assert obituario.place == "Capilla A"
    assert obituario.obituary_detail == "Mensaje de prueba para el obituario."
