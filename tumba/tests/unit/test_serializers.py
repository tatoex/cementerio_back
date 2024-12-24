import pytest
from tumba.serializers import TumbaSerializer, LoteSerializer

@pytest.mark.django_db
def test_lote_serializer():
    data = {
        'blockName': 1,
        'typeblock': "A",
        'numbersblock': 10,
        'filas': 5,
        'columnas': 2,
        'limite': 20
    }
    serializer = LoteSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data['blockName'] == 1

@pytest.mark.django_db
def test_tumba_serializer(lote):  # El fixture "lote" usa la base de datos
    data = {
        'nicheNumber': 1,
        'nicheType': 'T',
        'available': True,
        'nameLote': lote.id
    }
    serializer = TumbaSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data['nicheType'] == 'T'

@pytest.mark.django_db
def test_invalid_tumba_serializer():
    data = {
        'nicheNumber': -1,  # Inválido
        'nicheType': 'X',  # Inválido
        'available': True,
        'nameLote': 99999  # Lote inexistente
    }
    serializer = TumbaSerializer(data=data)
    assert not serializer.is_valid()
    assert 'nicheNumber' in serializer.errors
    assert 'nicheType' in serializer.errors
    assert 'nameLote' in serializer.errors

@pytest.mark.django_db
def test_invalid_tumba_nicheNumber(lote):
    data = {
        'nicheNumber': 0,  # Inválido
        'nicheType': 'T',
        'available': True,
        'nameLote': lote.id
    }
    serializer = TumbaSerializer(data=data)
    assert not serializer.is_valid()
    assert 'nicheNumber' in serializer.errors

