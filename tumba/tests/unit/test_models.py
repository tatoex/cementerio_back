import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from tumba.models import Lote, Tumba

# Fixture para crear un Lote reutilizable en las pruebas
@pytest.fixture
def lote():
    return Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=4,
        limite=20
    )

# Prueba de creación de un Lote
@pytest.mark.django_db
def test_lote_creation():
    lote = Lote.objects.create(
        blockName=1,
        typeblock="A",
        numbersblock=10,
        filas=5,
        columnas=2,
        limite=20
    )
    assert lote.blockName == 1
    assert lote.limite == 20
    assert lote.numbersblock == 10
    assert lote.filas == 5
    assert lote.columnas == 2

# Prueba de creación de una Tumba
@pytest.mark.django_db
def test_tumba_creation(lote):
    tumba = Tumba.objects.create(
        nicheNumber=1,
        nicheType='T',
        available=True,
        nameLote=lote  # Pasamos el Lote creado con la fixture
    )
    assert tumba.nicheNumber == 1
    assert tumba.available is True
    assert tumba.nicheType == 'T'
    assert tumba.nameLote == lote

# Prueba de propiedades ocupadas y disponibles en Lote
@pytest.mark.django_db
def test_lote_ocupadas_disponibles(lote):
    # Crear varias Tumbas en el Lote
    Tumba.objects.create(nicheNumber=1, nicheType='T', available=True, nameLote=lote)  # Disponible
    Tumba.objects.create(nicheNumber=2, nicheType='T', available=False, nameLote=lote)  # Ocupada
    Tumba.objects.create(nicheNumber=3, nicheType='T', available=False, nameLote=lote)  # Ocupada

    # Verificar las cantidades de tumbas ocupadas y disponibles
    assert lote.ocupadas() == 2  # Dos tumbas ocupadas
    assert lote.disponibles() == 1  # Una tumba disponible

@pytest.mark.django_db
def test_delete_lote_cascade_tumbas():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=20)
    Tumba.objects.create(nicheNumber=1, nicheType='T', available=True, nameLote=lote)
    lote.delete()
    assert Tumba.objects.count() == 0  # Todas las tumbas deben eliminarse

@pytest.mark.django_db
def test_update_lote_limit_affects_tumbas():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=2)
    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    Tumba.objects.create(nicheNumber=2, nicheType="T", available=True, nameLote=lote)

    # Intentar aumentar el límite y verificar que las tumbas existentes no se vean afectadas
    lote.limite = 5
    lote.save()

    assert lote.tumbaLote.count() == 2

@pytest.mark.django_db
def test_exceed_lote_limit(lote):
    lote.limite = 2
    lote.save()

    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    Tumba.objects.create(nicheNumber=2, nicheType="T", available=True, nameLote=lote)

    with pytest.raises(ValidationError, match="se ha alcanzado el límite del lote"):
        Tumba.objects.create(nicheNumber=3, nicheType="T", available=True, nameLote=lote)


@pytest.mark.django_db
def test_lote_limit_zero():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=0)
    with pytest.raises(Exception):
        Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)

@pytest.mark.django_db
def test_update_lote_limit_to_less_than_existing_tumbas():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=3)
    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    Tumba.objects.create(nicheNumber=2, nicheType="T", available=True, nameLote=lote)
    Tumba.objects.create(nicheNumber=3, nicheType="T", available=True, nameLote=lote)

    # Intentar reducir el límite a menos tumbas de las existentes
    lote.limite = 2
    with pytest.raises(ValidationError, match="El límite no puede ser menor que las tumbas existentes."):
        lote.save()
        
@pytest.mark.django_db
def test_unique_niche_number_in_lote(lote):
    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    with pytest.raises(IntegrityError):
        Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
