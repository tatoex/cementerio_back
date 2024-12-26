import pytest
from obituarios.serializers import ObituarioSerializer, MemoriaSerializer, EtapasObituarioSerializer
from django.utils.timezone import now


# ObituarioSerializer Tests
@pytest.mark.django_db
def test_obituario_serializer_to_json(obituario):
    serializer = ObituarioSerializer(instance=obituario)
    data = serializer.data
    assert data['obituary_detail'] == "Detalle del obituario"
    assert data['deceased'] == obituario.deceased.id

@pytest.mark.django_db
def test_obituario_serializer_from_json(difunto):
    data = {
        "obituary_detail": "Detalle nuevo",
        "deceased": difunto.id,
        "date_dead": now().isoformat(),
        "date_born": now().isoformat()
    }
    serializer = ObituarioSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    obituario = serializer.save()
    assert obituario.obituary_detail == "Detalle nuevo"

@pytest.mark.django_db
def test_obituario_serializer_rejects_extra_fields(difunto):
    data = {
        "obituary_detail": "Detalle extra",
        "deceased": difunto.id,
        "extra_field": "No permitido"
    }
    serializer = ObituarioSerializer(data=data)
    assert not serializer.is_valid()
    assert "Campos no válidos" in serializer.errors["non_field_errors"][0]
    
# MemoriaSerializer Tests
@pytest.mark.django_db
def test_memoria_serializer_to_json(memoria):
    serializer = MemoriaSerializer(instance=memoria)
    data = serializer.data
    assert data['names'] == "Carlos Sanchez"

@pytest.mark.django_db
def test_memoria_serializer_from_json(obituario):
    data = {
        "names": "Nuevo Autor",
        "text": "Nuevo Recuerdo",
        "obituary": obituario.id
    }
    serializer = MemoriaSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    memoria = serializer.save()
    assert memoria.text == "Nuevo Recuerdo"

# EtapasObituarioSerializer Tests
@pytest.mark.django_db
def test_etapas_obituario_serializer_to_json(etapa_obituario):
    serializer = EtapasObituarioSerializer(instance=etapa_obituario)
    data = serializer.data
    assert data['stage_ceremony'] == "Misa"

@pytest.mark.django_db
def test_etapas_obituario_serializer_valid_choices(obituario):
    data = {
        "stage_ceremony": "Misa",
        "place": "Iglesia Central",
        "obituary": obituario.id
    }
    serializer = EtapasObituarioSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    etapa = serializer.save()
    assert etapa.stage_ceremony == "Misa"

@pytest.mark.django_db
def test_etapas_obituario_serializer_invalid_choices(obituario):
    data = {
        "stage_ceremony": "Ceremonia Desconocida",
        "place": "Lugar Desconocido",
        "obituary": obituario.id
    }
    serializer = EtapasObituarioSerializer(data=data)
    assert not serializer.is_valid()
    assert "stage_ceremony" in serializer.errors
