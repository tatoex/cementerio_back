import pytest
from rest_framework.test import APIClient
from datetime import timedelta
from django.utils.timezone import now
from obituarios.models import Obituario


@pytest.mark.django_db
def test_full_flow_obituario_creation(difunto):

    # Crear un obituario utilizando el fixture `difunto`
    obituario = Obituario.objects.create(
        obituary_detail="Mensaje de prueba para el obituario.",
        cementery="Cementerio General",
        place="Capilla A",
        name="María Gómez",
        deceased=difunto,
        date_dead=now(),
        date_born=now() - timedelta(days=365 * 50)  # Simulando que nació hace 50 años
    )

    # Verificar que el obituario se creó correctamente
    assert obituario.deceased == difunto
    assert obituario.name == "María Gómez"
    assert obituario.cementery == "Cementerio General"
    assert obituario.place == "Capilla A"
    assert obituario.obituary_detail == "Mensaje de prueba para el obituario."
