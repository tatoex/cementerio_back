import pytest
from unittest.mock import patch
from django.db import IntegrityError
from threading import Thread
from tumba.models import Lote, Tumba


@pytest.mark.django_db
def test_database_failure_on_create_tumba():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=10)

    # Simular desconexión de la base de datos
    with patch("django.db.models.query.QuerySet.create", side_effect=Exception("Database error")):
        with pytest.raises(Exception, match="Database error"):
            Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)

