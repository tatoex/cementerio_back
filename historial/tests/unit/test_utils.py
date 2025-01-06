import pytest
from datetime import datetime, timedelta
from django.utils.timezone import now
from historial.utils import obtener_historial_limitado, compara_varias_versiones
from servicio.models import Servicio

@pytest.mark.django_db
def test_obtener_historial_limitado_insuficientes_versiones(servicio):
    # Verificar que no hay suficientes versiones
    with pytest.raises(ValueError, match="No hay suficientes versiones para comparar."):
        obtener_historial_limitado(Servicio, servicio.id, limit=5)

@pytest.mark.django_db
def test_obtener_historial_limitado_suficientes_versiones(servicio):
    # Realizar un cambio en el servicio
    servicio.description = "Servicio actualizado"
    servicio.save()

    # Verificar que se obtienen las versiones correctas
    historial = obtener_historial_limitado(Servicio, servicio.id, limit=5)
    assert len(historial) == 2  # Creación y actualización

@pytest.mark.django_db
def test_compara_varias_versiones_todos_los_campos(servicio):
    # Realizar un cambio en el servicio
    servicio.description = "Servicio actualizado"
    servicio.save()

    # Comparar todas las versiones
    cambios = compara_varias_versiones(Servicio, servicio.id, attribute="all", limit=5)
    assert len(cambios) == 1
    assert cambios[0]["cambios"][0]["campo"] == "description"
    assert cambios[0]["cambios"][0]["antes"] == "Servicio inicial"
    assert cambios[0]["cambios"][0]["despues"] == "Servicio actualizado"

@pytest.mark.django_db
def test_compara_varias_versiones_atributo_especifico(servicio):
    # Realizar un cambio en el atributo 'amount_paid'
    servicio.amount_paid = 150.00
    servicio.save()

    # Comparar el atributo 'amount_paid'
    cambios = compara_varias_versiones(Servicio, servicio.id, attribute="amount_paid", limit=5)
    assert len(cambios) == 1
    assert cambios[0]["cambios"][0]["campo"] == "amount_paid"
    assert cambios[0]["cambios"][0]["antes"] == 100.00
    assert cambios[0]["cambios"][0]["despues"] == 150.00
