import pytest
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, Lote
from django.core.exceptions import ValidationError

# Pruebas para Deudo
@pytest.mark.django_db
def test_deudo_required_fields():
    with pytest.raises(ValidationError):
        deudo = Deudo(
            last_names="Doe",  # Falta el campo 'names'
            idNumber="1234567891"
        )
        deudo.full_clean()

@pytest.mark.django_db
def test_deudo_invalid_email(deudo):
    deudo.email = "invalid-email"
    with pytest.raises(ValidationError, match="Enter a valid email address."):
        deudo.full_clean()

@pytest.mark.django_db
def test_deudo_field_length():
    with pytest.raises(ValidationError):
        deudo = Deudo(
            names="John",
            last_names="Doe",
            idNumber="12345678901",  # Excede la longitud máxima
            phoneNumber="0987654321",
            email="john.doe@example.com",
            tipo="Familiar"
        )
        deudo.full_clean()

@pytest.mark.django_db
def test_deudo_default_address(deudo):
    assert deudo.address == "Quito"

@pytest.mark.django_db
def test_deudo_history(deudo):
    initial_load_date = deudo.loadDate

    deudo.names = "Johnny"
    deudo.save()
    assert deudo.history.count() == 2
    assert deudo.history.first().names == "Johnny"
    assert deudo.history.first().loadDate == initial_load_date  # Asegura que loadDate no cambió
    
# Pruebas para Difunto
@pytest.mark.django_db
def test_difunto_required_fields(deudo, tumba):
    with pytest.raises(ValidationError):
        difunto = Difunto(
            last_names="Pérez",  # Falta el campo 'names'
            idNumber="0987654321",
            requestNumber="REQ002",
            tumba=tumba,
            deudo=deudo
        )
        difunto.full_clean()

@pytest.mark.django_db
def test_difunto_missing_deudo(tumba):
    with pytest.raises(ValidationError):
        difunto = Difunto(
            names="Juan",
            last_names="Pérez",
            idNumber="0987654321",
            requestNumber="REQ002",
            tumba=tumba
        )
        difunto.full_clean()


@pytest.mark.django_db
def test_difunto_default_description(deudo, tumba):
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ003",
        tumba=tumba,
        deudo=deudo
    )
    assert difunto.description == "N/A"

@pytest.mark.django_db
def test_difunto_history(deudo, tumba):
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ003",
        tumba=tumba,
        deudo=deudo
    )
    initial_load_date = difunto.loadDate

    difunto.names = "Pedro"
    difunto.save()
    assert difunto.history.count() == 2
    assert difunto.history.first().names == "Pedro"
    assert difunto.history.first().loadDate == initial_load_date  # Asegura que loadDate no cambió

@pytest.mark.django_db
def test_create_deudo(deudo):
    assert deudo.names == "John"
    assert deudo.tipo == "Familiar"

@pytest.mark.django_db
def test_create_difunto(deudo, tumba):
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )
    assert difunto.tumba == tumba
    assert difunto.deudo == deudo

@pytest.mark.django_db
def test_unique_id_number(deudo):
    nuevo_deudo = Deudo(
        names="Jane",
        last_names="Smith",
        idNumber="1234567890",  # Mismo ID que el deudo anterior
        phoneNumber="0987654322",
        email="jane.smith@example.com",
        address="Quito",
        tipo="Conocido"
    )
    with pytest.raises(ValidationError, match="El ID 1234567890 ya está en uso por otro deudo."):
        nuevo_deudo.full_clean()
        nuevo_deudo.save()

@pytest.mark.django_db
def test_difunto_with_tumba(deudo, tumba):
    difunto = Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654322",
        requestNumber="REQ003",
        tumba=tumba,
        deudo=deudo
    )
    assert difunto.tumba == tumba

@pytest.mark.django_db
def test_deudo_tipo_choices(deudo):
    deudo.tipo = "Conocido"
    deudo.save()
    assert deudo.tipo == "Conocido"
    with pytest.raises(ValidationError):
        deudo.tipo = "Invalido"  # Valor no permitido
        deudo.full_clean()