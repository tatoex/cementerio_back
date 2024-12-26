import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from obituarios.models import Obituario, Memoria, EtapasObituario
from difunto.models import Difunto
from django.utils.timezone import now


@pytest.mark.django_db
class TestObituario:
    def test_create_obituario(self, difunto):
        obituario = Obituario.objects.create(
            obituary_detail="Detalle del obituario de prueba.",
            cementery="Cementerio Central",
            place="Capilla",
            name="Juan Perez",
            deceased=difunto,
            date_dead=now(),
            date_born=now()
        )
        assert obituario.obituary_detail == "Detalle del obituario de prueba."

    def test_long_text_obituary_detail(self, difunto):
        long_text = "Texto " * 500  # Crear un texto largo
        obituario = Obituario.objects.create(
            obituary_detail=long_text,
            deceased=difunto,
        )
        assert len(obituario.obituary_detail) == len(long_text)


    def test_str_method(self, difunto):
        obituario = Obituario.objects.create(
            obituary_detail="Detalle del obituario",
            deceased=difunto
        )
        assert str(obituario) == f"Obituario de {difunto.names} {difunto.last_names}"

@pytest.mark.django_db
class TestMemoria:
    def test_create_memoria(self, obituario):
        memoria = Memoria.objects.create(
            names="Carlos Sánchez",
            relationship="Hermano",
            text="Te extrañaremos siempre.",
            obituary=obituario
        )
        assert memoria.text == "Te extrañaremos siempre."


    def test_obituario_details_property(self, obituario):
        memoria = Memoria.objects.create(
            names="Carlos Sánchez",
            text="Recuerdo con detalles.",
            obituary=obituario
        )
        assert memoria.obituarioDetails == f"{obituario.deceased.names} {obituario.deceased.last_names}"

    def test_str_method(self, obituario):
        memoria = Memoria.objects.create(
            names="Carlos Sánchez",
            text="Recuerdo con detalles.",
            obituary=obituario
        )
        assert str(memoria) == f"Recuerdo de Carlos Sánchez para {obituario.deceased.names} {obituario.deceased.last_names}"


@pytest.mark.django_db
class TestEtapasObituario:
    def test_valid_choices(self, obituario):
        etapa = EtapasObituario.objects.create(
            stage_ceremony="Misa",
            place="Capilla Principal",
            obituary=obituario
        )
        assert etapa.stage_ceremony == "Misa"

    def test_invalid_choices(self, obituario):
        with pytest.raises(ValidationError):
            etapa = EtapasObituario(
                stage_ceremony="Evento Invalido",
                place="Lugar desconocido",
                obituary=obituario
            )
            etapa.full_clean()  # Ejecutar validación manualmente

    def test_foreign_key_relationship(self, obituario):
        etapa = EtapasObituario.objects.create(
            stage_ceremony="Velacion",
            place="Capilla Secundaria",
            obituary=obituario
        )
        assert etapa.obituary == obituario

    def test_str_method(self, obituario):
        etapa = EtapasObituario.objects.create(
            stage_ceremony="Misa",
            place="Capilla Principal",
            obituary=obituario
        )
        assert str(etapa) == f"Misa en Capilla Principal para {obituario.deceased.names} {obituario.deceased.last_names}"
