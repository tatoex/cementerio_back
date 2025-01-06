import pytest
from obituarios.models import EtapasObituario


@pytest.mark.django_db
def test_historical_difunto_creation(difunto):
    historial = difunto.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_obituario_update(obituario):
    obituario.obituary_detail = "Detalle actualizado"
    obituario.save()
    historial = obituario.history.all()
    assert historial.count() == 2  # Uno por la creación y otro por la actualización


@pytest.mark.django_db
def test_historical_etapas_obituario_creation(obituario):
    etapa = EtapasObituario.objects.create(
        stage_ceremony="Misa",
        place="Capilla Principal",
        obituary=obituario
    )
    historial = etapa.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_lote_creation(lote):
    historial = lote.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_tumba_creation(tumba):
    historial = tumba.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_deudo_creation(deudo):
    historial = deudo.history.all()
    assert historial.count() == 1


@pytest.mark.django_db
def test_historical_lote_update(lote):
    lote.filas = 6
    lote.save()
    historial = lote.history.all()
    assert historial.count() == 2  # Uno por la creación y otro por la actualización


@pytest.mark.django_db
def test_historical_tumba_update(tumba):
    tumba.available = False
    tumba.save()
    historial = tumba.history.all()
    assert historial.count() == 2  # Uno por la creación y otro por la actualización


@pytest.mark.django_db
def test_historical_deudo_update(deudo):
    deudo.address = "Guayaquil"
    deudo.save()
    historial = deudo.history.all()
    assert historial.count() == 2  # Uno por la creación y otro por la actualización


@pytest.mark.django_db
def test_historical_servicio_creation(servicio):
    historial = servicio.history.all()
    assert historial.count() == 1  # Solo debe haber una entrada en el historial


@pytest.mark.django_db
def test_historical_servicio_update(servicio):
    servicio.description = "Servicio actualizado"
    servicio.save()
    historial = servicio.history.all()
    assert historial.count() == 2  # Una entrada para la creación y otra para la actualización
