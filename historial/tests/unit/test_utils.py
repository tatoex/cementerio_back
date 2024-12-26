import pytest
from datetime import datetime, timedelta
from django.utils.timezone import now
from historial.utils import obtener_historial_limitado, compara_varias_versiones
from servicio.models import Servicio
from tumba.models import Tumba, Lote
from difunto.models import Difunto, Deudo


@pytest.mark.django_db
def test_obtener_historial_limitado_insuficientes_versiones():
    # Crear relaciones necesarias
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ001", deudo=deudo, tumba=tumba
    )

    # Crear un servicio sin suficientes cambios históricos
    servicio = Servicio.objects.create(
        startDate=now(),
        endDate=now() + timedelta(days=7),
        ceremony="Inhumacion",
        is_paid=True,
        amount_paid=100.00,
        description="Servicio inicial",
        numberTomb=tumba,
        deceased=difunto
    )

    # Verificar que no hay suficientes versiones
    with pytest.raises(ValueError, match="No hay suficientes versiones para comparar."):
        obtener_historial_limitado(Servicio, servicio.id, limit=5)


@pytest.mark.django_db
def test_obtener_historial_limitado_suficientes_versiones():
    # Crear relaciones necesarias
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ001", deudo=deudo, tumba=tumba
    )

    # Crear un servicio y realizar un cambio
    servicio = Servicio.objects.create(
        startDate=now(),  # Cambiado de datetime.now() a now()
        endDate=now() + timedelta(days=7),
        ceremony="Inhumacion",
        is_paid=True,
        amount_paid=100.00,
        description="Servicio inicial",
        numberTomb=tumba,
        deceased=difunto
    )
    servicio.description = "Servicio actualizado"
    servicio.save()

    # Verificar que se obtienen las versiones correctas
    historial = obtener_historial_limitado(Servicio, servicio.id, limit=5)
    assert len(historial) == 2  # Creación y actualización


@pytest.mark.django_db
def test_compara_varias_versiones_todos_los_campos():
    # Crear relaciones necesarias
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ001", deudo=deudo, tumba=tumba
    )

    # Crear un servicio y realizar un cambio
    servicio = Servicio.objects.create(
        startDate=now(),
        endDate=now() + timedelta(days=7),
        ceremony="Inhumacion",
        is_paid=True,
        amount_paid=100.00,
        description="Servicio inicial",
        numberTomb=tumba,
        deceased=difunto
    )
    servicio.description = "Servicio actualizado"
    servicio.save()

    # Comparar todas las versiones
    cambios = compara_varias_versiones(Servicio, servicio.id, attribute="all", limit=5)
    assert len(cambios) == 1
    assert cambios[0]["cambios"][0]["campo"] == "description"
    assert cambios[0]["cambios"][0]["antes"] == "Servicio inicial"
    assert cambios[0]["cambios"][0]["despues"] == "Servicio actualizado"


@pytest.mark.django_db
def test_compara_varias_versiones_atributo_especifico():
    # Crear relaciones necesarias
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)
    tumba = Tumba.objects.create(nicheNumber=1, nicheType="E", available=True, nameLote=lote)
    deudo = Deudo.objects.create(
        names="John", last_names="Doe", idNumber="1234567890",
        phoneNumber="0987654321", email="john.doe@example.com",
        address="Quito", tipo="Familiar"
    )
    difunto = Difunto.objects.create(
        names="Maria", last_names="Gomez", idNumber="123456789",
        requestNumber="REQ001", deudo=deudo, tumba=tumba
    )

    # Crear un servicio y realizar un cambio
    servicio = Servicio.objects.create(
        startDate=now(),
        endDate=now() + timedelta(days=7),
        ceremony="Inhumacion",
        is_paid=True,
        amount_paid=100.00,
        description="Servicio inicial",
        numberTomb=tumba,
        deceased=difunto
    )
    servicio.amount_paid = 150.00
    servicio.save()

    # Comparar el atributo 'amount_paid'
    cambios = compara_varias_versiones(Servicio, servicio.id, attribute="amount_paid", limit=5)
    assert len(cambios) == 1
    assert cambios[0]["cambios"][0]["campo"] == "amount_paid"
    assert cambios[0]["cambios"][0]["antes"] == 100.00  # Ahora se compara con un Decimal
    assert cambios[0]["cambios"][0]["despues"] == 150.00