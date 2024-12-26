import pytest
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from difunto.models import Deudo, Difunto
from tumba.models import Lote, Tumba
from obituarios.models import Obituario, EtapasObituario
from servicio.models import Servicio
@pytest.mark.django_db
def test_historical_difunto_creation():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Juan", last_names="Pérez", idNumber="0987654321",
        requestNumber="REQ001", tumba=tumba, deudo=deudo
    )
    historial = difunto.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_obituario_update():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ002", deudo=deudo, tumba=tumba
    )
    obituario = Obituario.objects.create(
        obituary_detail="Detalles", cementery="Cementerio Central",
        place="Capilla 1", name="Maria Gomez", deceased=difunto
    )
    obituario.obituary_detail = "Detalle actualizado"
    obituario.save()
    historial = obituario.history.all()
    assert historial.count() == 2


@pytest.mark.django_db
def test_historical_etapas_obituario_creation():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ002", deudo=deudo, tumba=tumba
    )
    obituario = Obituario.objects.create(
        obituary_detail="Detalles", cementery="Cementerio Central",
        place="Capilla 1", name="Maria Gomez", deceased=difunto
    )
    etapa = EtapasObituario.objects.create(
        stage_ceremony="Misa", place="Capilla Principal", obituary=obituario
    )
    historial = etapa.history.all()
    assert historial.count() == 1

@pytest.mark.django_db
def test_historical_lote_creation():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    historial = lote.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_tumba_creation():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    historial = tumba.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_deudo_creation():
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    historial = deudo.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_lote_update():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    lote.filas = 6
    lote.save()
    historial = lote.history.all()
    assert historial.count() == 2  # Uno por la creación y otro por la actualización


@pytest.mark.django_db
def test_historical_tumba_update():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    tumba.available = False
    tumba.save()
    historial = tumba.history.all()
    assert historial.count() == 2  # Uno por la creación y otro por la actualización


@pytest.mark.django_db
def test_historical_deudo_update():
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    deudo.address = "Guayaquil"
    deudo.save()
    historial = deudo.history.all()
    assert historial.count() == 2  # Uno por la creación y otro por la actualización

@pytest.mark.django_db
def test_historical_servicio_creation():
    # Crear objetos relacionados
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ002", deudo=deudo, tumba=tumba
    )

    # Crear un objeto Servicio
    servicio = Servicio.objects.create(
        startDate=now(),
        endDate=now(),
        ceremony="Inhumacion",
        is_paid=False,
        amount_paid=Decimal("1.10"),
        payment_date=now(),
        description="Servicio de prueba",
        numberTomb=tumba,
        deceased=difunto
    )

    # Verificar historial
    historial = servicio.history.all()
    assert historial.count() == 1  # Solo debe haber una entrada en el historial


@pytest.mark.django_db
def test_historical_servicio_update():
    # Crear objetos relacionados
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ002", deudo=deudo, tumba=tumba
    )

    # Crear y actualizar un objeto Servicio
    servicio = Servicio.objects.create(
        startDate=now(),
        endDate=now(),
        ceremony="Inhumacion",
        is_paid=False,
        amount_paid=Decimal("1.10"),
        payment_date=now(),
        description="Servicio inicial",
        numberTomb=tumba,
        deceased=difunto
    )
    servicio.description = "Servicio actualizado"
    servicio.save()

    # Verificar historial
    historial = servicio.history.all()
    assert historial.count() == 2  # Una entrada para la creación y otra para la actualización