import pytest
from difunto.models import Difunto, Deudo
from difunto.serializers import DeudoSerializer, DifuntoSerializer
from rest_framework.exceptions import ValidationError


@pytest.mark.django_db
def test_deudo_serializer_fields(deudo):
    serializer = DeudoSerializer(instance=deudo)
    data = serializer.data
    assert set(data.keys()) == {"id", "names", "last_names", "idNumber", "phoneNumber", "email", "address", "tipo", "description"}


@pytest.mark.django_db
def test_difunto_serializer_with_relations(deudo, tumba):
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    serializer = DifuntoSerializer(instance=difunto)
    data = serializer.data
    assert data["tumba_ob"]["nicheNumber"] == tumba.nicheNumber
    assert data["deudo_ob"]["names"] == deudo.names


@pytest.mark.django_db
def test_deudo_serializer_missing_fields():
    data = {"last_names": "Doe", "phoneNumber": "0987654321"}
    serializer = DeudoSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_difunto_serializer_missing_fields(deudo):
    data = {"names": "Juan", "last_names": "Pérez", "deudo": deudo.id}
    serializer = DifuntoSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)

@pytest.mark.django_db
def test_deudo_serializer_valid(deudo):
    serializer = DeudoSerializer(instance=deudo)
    data = serializer.data
    assert data["idNumber"] == "1234567890"

@pytest.mark.django_db
def test_difunto_serializer_valid(deudo, tumba):
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    serializer = DifuntoSerializer(instance=difunto)
    data = serializer.data
    assert data["tumba"] == tumba.id

@pytest.mark.django_db
def test_difunto_serializer_invalid(deudo):
    serializer = DifuntoSerializer(data={
        "names": "Juan",
        "last_names": "Pérez",
        "idNumber": "0987654321",
        "deudo": deudo.id,
        "requestNumber": ""
    })
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
