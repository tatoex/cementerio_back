import pytest
from obituarios.models import Memoria, EtapasObituario


@pytest.mark.django_db
def test_historical_servicio_serializer(servicio):
    # Verificar que el historial se haya creado
    historial = servicio.history.all()
    assert historial.count() == 1
    assert historial.first().ceremony == "Inhumacion"
    assert historial.first().history_type == "+"


@pytest.mark.django_db
def test_historical_tumba_serializer(tumba):
    # Verificar que el historial se haya creado
    historial = tumba.history.all()
    assert historial.count() == 1
    assert historial.first().nicheType == "E"
    assert historial.first().history_type == "+"


@pytest.mark.django_db
def test_historical_deudo_serializer(deudo):
    # Verificar que el historial se haya creado
    historial = deudo.history.all()
    assert historial.count() == 1
    assert historial.first().names == "John"
    assert historial.first().history_type == "+"


@pytest.mark.django_db
def test_historical_lote_serializer(lote):
    # Verificar que el historial se haya creado
    historial = lote.history.all()
    assert historial.count() == 1
    assert historial.first().blockName == 1
    assert historial.first().typeblock == "A"
    assert historial.first().history_type == "+"


@pytest.mark.django_db
def test_historical_difunto_serializer(difunto):
    # Verificar que el historial se haya creado
    historial = difunto.history.all()
    assert historial.count() == 1
    assert historial.first().names == "Maria"
    assert historial.first().history_type == "+"


@pytest.mark.django_db
def test_historical_obituario_serializer(obituario):
    # Verificar que el historial se haya creado
    historial = obituario.history.all()
    assert historial.count() == 1
    assert historial.first().obituary_detail == "Mensaje de prueba para el obituario."
    assert historial.first().history_type == "+"


@pytest.mark.django_db
def test_historical_memoria_serializer(obituario):
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
def test_historical_etapas_obituario_serializer(obituario):
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

