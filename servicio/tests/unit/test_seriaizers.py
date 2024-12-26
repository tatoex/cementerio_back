import pytest
from rest_framework.exceptions import ValidationError
from servicio.serializers import (
    ServicioSerializer, 
    ServicioEstadoSerializer, 
    TumbaEstadoSerializer
)
from decimal import Decimal
from django.utils.timezone import now as timezone_now

@pytest.mark.django_db
def test_servicio_serializer_creation(tumba, difunto):
    data = {
        "startDate": timezone_now(),
        "ceremony": "Inhumacion",
        "is_paid": False,
        "amount_paid": "100.50",
        "numberTomb": tumba.id,
        "deceased": difunto.id
    }
    serializer = ServicioSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert instance.ceremony == "Inhumacion"
    assert instance.amount_paid == Decimal("100.50")

@pytest.mark.django_db
def test_servicio_estado_serializer(servicio):
    serializer = ServicioEstadoSerializer(servicio)
    expected_data = {
        "startDate": servicio.startDate.isoformat().replace('+00:00', 'Z'),
        "endDate": servicio.endDate.isoformat().replace('+00:00', 'Z') if servicio.endDate else None,
        "ceremony": "Inhumacion"
    }
    assert serializer.data == expected_data

@pytest.mark.django_db
def test_tumba_estado_serializer(tumba, servicio):
    serializer = TumbaEstadoSerializer(tumba)
    assert serializer.data["nicheNumber"] == tumba.nicheNumber
    assert serializer.data["nicheType"] == tumba.nicheType
    assert serializer.data["available"] == tumba.available
    assert "difunto" in serializer.data
    assert "servicio" in serializer.data

@pytest.mark.django_db
def test_servicio_serializer_invalid_data(tumba, difunto):
    data = {
        "startDate": timezone_now(),
        "ceremony": "InvalidCeremony",
        "is_paid": False,
        "amount_paid": "-100.50",
        "numberTomb": tumba.id,
        "deceased": difunto.id
    }
    serializer = ServicioSerializer(data=data)
    assert not serializer.is_valid()
    assert "ceremony" in serializer.errors
    assert "amount_paid" in serializer.errors

@pytest.mark.django_db
def test_servicio_serializer_partial_update(servicio):
    data = {
        "is_paid": True,
        "amount_paid": "200.00"
    }
    serializer = ServicioSerializer(servicio, data=data, partial=True)
    assert serializer.is_valid(), serializer.errors
    updated_instance = serializer.save()
    assert updated_instance.is_paid is True
    assert updated_instance.amount_paid == Decimal("200.00")
