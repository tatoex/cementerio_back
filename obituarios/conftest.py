import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from obituarios.models import Obituario, Memoria, EtapasObituario
from django.utils.timezone import now
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, Lote

# Imagen de prueba para los modelos que la requieran
@pytest.fixture
def test_image():
    return SimpleUploadedFile(
        name="test_image.jpg",
        content=b"file_content",
        content_type="image/jpeg"
    )

# Cliente API para pruebas
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def deudo():
    return Deudo.objects.create(
        names="John",
        last_names="Doe",
        idNumber="1234567890",
        phoneNumber="0987654321",
        email="john.doe@example.com",
        address="Quito",
        tipo="Familiar"
    )

@pytest.fixture
def lote():
    return Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=4, limite=20)

@pytest.fixture
def tumba(lote):
    return Tumba.objects.create(
        nicheNumber=1,
        nicheType="E",
        available=True,
        nameLote=lote
    )

@pytest.fixture
def difunto(deudo, tumba):
    return Difunto.objects.create(
        names="Juan",
        last_names="Perez",
        idNumber="0987654321",
        requestNumber="REQ001",
        tumba=tumba,
        deudo=deudo
    )

# Fixture para el modelo Obituario
@pytest.fixture
def obituario(difunto, test_image):
    return Obituario.objects.create(
        obituary_detail="Detalle del obituario",
        cementery="Cementerio Central",
        place="Capilla Principal",
        name="Juan Perez",
        deceased=difunto,
        image_dif=test_image,
        date_dead=now(),
        date_born=now()
    )

# Fixture para el modelo Memoria
@pytest.fixture
def memoria(obituario, test_image):
    return Memoria.objects.create(
        names="Carlos Sanchez",
        relationship="Amigo",
        text="Un hermoso recuerdo para siempre",
        image=test_image,
        obituary=obituario
    )

# Fixture para el modelo EtapasObituario
@pytest.fixture
def etapa_obituario(obituario):
    return EtapasObituario.objects.create(
        stage_ceremony="Misa",
        place="Capilla Principal",
        obituary=obituario
    )