import pytest
from rest_framework.test import APIClient
from rest_framework import status
from tumba.models import Lote, Tumba

@pytest.mark.django_db
def test_filter_tumba_by_niche_type():
    lote = Lote.objects.create(blockName=1, typeblock="A", numbersblock=10, filas=5, columnas=2, limite=10)
    Tumba.objects.create(nicheNumber=1, nicheType="T", available=True, nameLote=lote)
    Tumba.objects.create(nicheNumber=2, nicheType="E", available=True, nameLote=lote)
    
    client = APIClient()
    response = client.get('/api/tumba/?nicheType=T')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['nicheType'] == "T"