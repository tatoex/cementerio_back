import pytest
from datetime import timedelta
from decimal import Decimal
from django.utils.timezone import now
from difunto.models import Deudo, Difunto
from tumba.models import Lote, Tumba
from servicio.models import Servicio
from obituarios.models import Obituario, Memoria, EtapasObituario

@pytest.mark.django_db
def test_historical_servicio_serializer():
    # Crear datos relacionados
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

    # Crear un servicio
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

    # Verificar que el historial se haya creado
    historial = servicio.history.all()
    assert historial.count() == 1
    assert historial.first().ceremony == "Inhumacion"
    assert historial.first().history_type == "+"

@pytest.mark.django_db
def test_historical_tumba_serializer():
    # Crear un lote
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

    # Crear una tumba
    tumba = Tumba.objects.create(
        nicheNumber=2,
        nicheType="E",
        available=True,
        nameLote=lote
    )

    # Verificar que el historial se haya creado
    historial = tumba.history.all()
    assert historial.count() == 1
    assert historial.first().nicheType == "E"
    assert historial.first().history_type == "+"

@pytest.mark.django_db
def test_historical_deudo_serializer():
    # Crear un deudo
    deudo = Deudo.objects.create(
        names="Ana",
        last_names="Perez",
        idNumber="0987654321",
        phoneNumber="0987654321",
        email="ana.perez@example.com",
        address="Quito",
        tipo="Familiar"
    )

    # Verificar que el historial se haya creado
    historial = deudo.history.all()
    assert historial.count() == 1
    assert historial.first().names == "Ana"
    assert historial.first().history_type == "+"

@pytest.mark.django_db
def test_historical_lote_serializer():
    # Crear un lote
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

    # Verificar que el historial se haya creado
    historial = lote.history.all()
    assert historial.count() == 1
    assert historial.first().blockName == 1
    assert historial.first().typeblock == "A"
    assert historial.first().history_type == "+"

@pytest.mark.django_db
def test_historical_difunto_serializer():
    # Crear datos relacionados
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )

    # Crear un difunto
    difunto = Difunto.objects.create(
        names="Maria",
        last_names="Gomez",
        idNumber="123456789",
        requestNumber="REQ002",
        deudo=deudo,
        tumba=tumba
    )

    # Verificar que el historial se haya creado
    historial = difunto.history.all()
    assert historial.count() == 1
    assert historial.first().names == "Maria"
    assert historial.first().history_type == "+"

@pytest.mark.django_db
def test_historical_obituario_serializer():
    # Crear datos relacionados
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria",
        last_names="Gomez",
        idNumber="123456789",
        requestNumber="REQ002",
        deudo=deudo,
        tumba=tumba
    )

    # Crear un obituario
    obituario = Obituario.objects.create(
        obituary_detail="Detalles del obituario",
        cementery="Cementerio Central",
        place="Capilla 1",
        name="Maria Gomez",
        deceased=difunto
    )

    # Verificar que el historial se haya creado
    historial = obituario.history.all()
    assert historial.count() == 1
    assert historial.first().obituary_detail == "Detalles del obituario"
    assert historial.first().history_type == "+"

@pytest.mark.django_db
def test_historical_memoria_serializer():
    # Crear datos relacionados
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria",
        last_names="Gomez",
        idNumber="123456789",
        requestNumber="REQ002",
        deudo=deudo,
        tumba=tumba
    )
    obituario = Obituario.objects.create(
        obituary_detail="Detalles del obituario",
        cementery="Cementerio Central",
        place="Capilla 1",
        name="Maria Gomez",
        deceased=difunto
    )

    # Crear una memoria
    memoria = Memoria.objects.create(
        names="Carlos",
        relationship="Amigo",
        text="Recuerdo especial",
        obituary=obituario
    )

    # Verificar que el historial se haya creado
    historial = memoria.history.all()
    assert historial.count() == 1
    assert historial.first().text == "Recuerdo especial"
    assert historial.first().history_type == "+"

@pytest.mark.django_db
def test_historical_etapas_obituario_serializer():
    # Crear datos relacionados
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria",
        last_names="Gomez",
        idNumber="123456789",
        requestNumber="REQ002",
        deudo=deudo,
        tumba=tumba
    )
    obituario = Obituario.objects.create(
        obituary_detail="Detalles del obituario",
        cementery="Cementerio Central",
        place="Capilla 1",
        name="Maria Gomez",
        deceased=difunto
    )

    # Crear una etapa del obituario
    etapa = EtapasObituario.objects.create(
        stage_ceremony="Misa",
        place="Capilla Principal",
        obituary=obituario
    )

    # Verificar que el historial se haya creado
    historial = etapa.history.all()
    assert historial.count() == 1
    assert historial.first().stage_ceremony == "Misa"
    assert historial.first().history_type == "+"
