import pytest
from django.contrib.auth.models import Group
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_list_groups_success():
    """
    Verifica que un usuario autenticado pueda listar los grupos existentes.
    """
    Group.objects.create(name="Administrador")
    Group.objects.create(name="Secretaria")

    client = APIClient()
    client.login(username="admin", password="adminpassword")

    response = client.get('/api/groups/')

    assert response.status_code == 200
    assert len(response.data) == 2
    assert any(group['name'] == "Administrador" for group in response.data)
    assert any(group['name'] == "Secretaria" for group in response.data)


@pytest.mark.django_db
def test_list_groups_unauthenticated():
    """
    Verifica que un usuario no autenticado no pueda listar los grupos.
    """
    client = APIClient()
    response = client.get('/api/groups/')

    assert response.status_code == 401
    assert "detail" in response.data
    assert response.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_retrieve_group_success():
    """
    Verifica que un usuario autenticado pueda recuperar los detalles de un grupo específico.
    """
    group = Group.objects.create(name="Administrador")

    client = APIClient()
    client.login(username="admin", password="adminpassword")

    response = client.get(f'/api/groups/{group.id}/')

    assert response.status_code == 200
    assert response.data['id'] == group.id
    assert response.data['name'] == "Administrador"


@pytest.mark.django_db
def test_retrieve_group_unauthenticated():
    """
    Verifica que un usuario no autenticado no pueda recuperar los detalles de un grupo específico.
    """
    group = Group.objects.create(name="Administrador")

    client = APIClient()
    response = client.get(f'/api/groups/{group.id}/')

    assert response.status_code == 401
    assert "detail" in response.data
    assert response.data["detail"] == "Authentication credentials were not provided."
