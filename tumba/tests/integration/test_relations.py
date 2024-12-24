import pytest
from tumba.models import Tumba, Lote

@pytest.mark.django_db
def test_lote_delete_cascade_tumbas():
    # Crear un lote con varias tumbas
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=20)
    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    Tumba.objects.create(nicheNumber=2, nicheType="T", available=True, nameLote=lote)

    # Guardar el ID del lote antes de eliminarlo
    lote_id = lote.id

    # Eliminar el lote
    lote.delete()

    # Verificar que todas las tumbas relacionadas también fueron eliminadas
    assert Tumba.objects.filter(nameLote_id=lote_id).count() == 0

@pytest.mark.django_db
def test_tumba_delete_does_not_affect_lote(lote):
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    tumba.delete()
    assert Lote.objects.filter(id=lote.id).exists()