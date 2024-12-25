import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from datetime import timedelta
from decimal import Decimal
from django.utils.timezone import now
from servicio.models import Servicio
from tumba.models import Tumba, Lote
from difunto.models import Difunto, Deudo

# Fixture para crear un objeto deudo
@pytest.fixture
def deudo():
    """
    Crea y devuelve un objeto Deudo para ser utilizado en las pruebas.
    """
    return Deudo.objects.create(
        names="John",
        last_names="Doe",
        idNumber="1234567890",
        phoneNumber="0987654321",
        email="john.doe@example.com",
        address="Quito",
        tipo="Familiar"
    )

# Fixture para crear un objeto lote
@pytest.fixture
def lote():
    """
    Crea y devuelve un objeto Lote con un blockName válido.
    """
    return Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

# Fixture para crear un objeto tumba asociado a un lote
@pytest.fixture
def tumba(lote):
    """
    Crea y devuelve un objeto Tumba asociado al lote proporcionado.
    """
    return Tumba.objects.create(
        id=6000,
        nicheNumber=0,
        nicheType="T",
        available=True,
        nameLote=lote
    )

# Fixture para crear un objeto difunto asociado a una tumba y un deudo
@pytest.fixture
def difunto(tumba, deudo):
    """
    Crea y devuelve un objeto Difunto asociado a una tumba y un deudo.
    """
    return Difunto.objects.create(
        names="Juan",
        last_names="Pérez",
        idNumber="0987654321",
        requestNumber="REQ001",
        deudo=deudo,
        tumba=tumba
    )

# Prueba para la creación de un servicio
@pytest.mark.django_db
def test_servicio_creation(deudo, difunto, tumba):
    """
    Prueba que un servicio pueda ser creado correctamente con datos válidos.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        endDate=now(),
        ceremony="Inhumacion",
        is_paid=True,
        amount_paid=100.50,
        payment_date=now(),
        description="Servicio de prueba",
        numberTomb=tumba,
        deceased=difunto
    )
    assert servicio.ceremony == "Inhumacion"
    assert servicio.is_paid is True

# Prueba para valores predeterminados en el modelo Servicio
@pytest.mark.django_db
def test_servicio_default_values(difunto):
    """
    Prueba que los valores predeterminados del modelo Servicio se configuren correctamente.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        deceased=difunto
    )
    assert servicio.amount_paid == Decimal("1.10")

# Prueba para verificar un valor inválido en el campo ceremony
@pytest.mark.django_db
def test_invalid_ceremony_choice(difunto):
    """
    Prueba que se lance una excepción si se proporciona un valor inválido para el campo 'ceremony'.
    """
    with pytest.raises(ValidationError, match="is not a valid choice"):
        Servicio.objects.create(
            startDate=now(),
            ceremony="Invalido",
            deceased=difunto
        )

# Prueba de relaciones entre Servicio, Tumba y Difunto
@pytest.mark.django_db
def test_servicio_relationships(difunto, tumba):
    """
    Prueba que un Servicio esté correctamente asociado a una Tumba y un Difunto.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        ceremony="Cremacion",
        numberTomb=tumba,
        deceased=difunto
    )
    assert servicio.numberTomb == tumba
    assert servicio.deceased == difunto

# Prueba para cambiar el estado de pago de un servicio
@pytest.mark.django_db
def test_servicio_payment_status(difunto):
    """
    Prueba que el estado de pago de un Servicio pueda ser actualizado.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        is_paid=False,
        deceased=difunto
    )
    servicio.is_paid = True
    servicio.save()
    assert servicio.is_paid is True

# Prueba para exceder el límite de amount_paid
@pytest.mark.django_db
def test_amount_paid_limit(difunto):
    """
    Prueba que se lance una excepción si el monto excede el límite permitido.
    """
    with pytest.raises(ValidationError):
        Servicio.objects.create(
            startDate=now(),
            amount_paid=Decimal("100000000.00"),
            deceased=difunto
        )

# Prueba para valores límite en amount_paid
@pytest.mark.django_db
def test_amount_paid_boundary_values(difunto):
    """
    Prueba que el campo amount_paid acepte el valor límite permitido.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        amount_paid=Decimal("99999999.99"),
        deceased=difunto
    )
    assert servicio.amount_paid == Decimal("99999999.99")

# Prueba para actualizar la fecha de modificación
@pytest.mark.django_db
def test_update_date_field(difunto):
    """
    Prueba que el campo updateDate se actualice al modificar el Servicio.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        deceased=difunto
    )
    initial_update_date = servicio.updateDate
    servicio.description = "Actualizado"
    servicio.save()
    assert servicio.updateDate > initial_update_date

# Prueba para rango de fechas inválido
@pytest.mark.django_db
def test_invalid_date_range(difunto):
    """
    Prueba que se lance una excepción si la fecha de fin es anterior a la fecha de inicio.
    """
    with pytest.raises(ValidationError, match="La fecha de vencimiento no puede ser anterior a la fecha de inicio"):
        Servicio.objects.create(
            startDate=now(),
            endDate=now() - timedelta(days=1),
            deceased=difunto
        )

# Prueba de campos opcionales
@pytest.mark.django_db
def test_servicio_with_optional_fields(difunto):
    """
    Prueba que los campos opcionales del Servicio se configuren correctamente.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        deceased=difunto,
        description=""
    )
    assert servicio.description == "N/A"

# Prueba para filtrar servicios por estado de pago
@pytest.mark.django_db
def test_filter_servicio_by_status(difunto):
    """
    Prueba que se puedan filtrar servicios completados por estado de pago.
    """
    Servicio.objects.create(startDate=now(), is_paid=True, endDate=now(), deceased=difunto)
    Servicio.objects.create(startDate=now(), is_paid=False, deceased=difunto)
    activos = Servicio.objects.filter(is_paid=True, endDate__isnull=False).count()
    assert activos == 1

# Prueba de relaciones inversas
@pytest.mark.django_db
def test_reverse_relationship(difunto, tumba):
    """
    Prueba que las relaciones inversas entre Servicio, Tumba y Difunto funcionen correctamente.
    """
    servicio = Servicio.objects.create(
        startDate=now(),
        numberTomb=tumba,
        deceased=difunto
    )
    assert tumba.servicioTumba.first() == servicio
    assert difunto.servicioDifunto.first() == servicio
