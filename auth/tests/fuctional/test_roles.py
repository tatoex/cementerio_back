import pytest
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_secretaria_access_allowed():
    """
    Verifica que un usuario en el grupo 'Secretaria' tenga acceso al endpoint correspondiente.
    """
    group = Group.objects.create(name="Secretaria")
    user = User.objects.create_user(username="secretaria_user", password="securepassword")
    user.groups.add(group)

    client = APIClient()
    client.login(username="secretaria_user", password="securepassword")

    response = client.get('/api/secretaria/')

    assert response.status_code == 200
    assert response.data.get("message") == "Acceso permitido a Secretaría"
    assert response.data.get("user") == "secretaria_user"


@pytest.mark.django_db
def test_secretaria_access_denied():
    """
    Verifica que un usuario fuera del grupo 'Secretaria' no tenga acceso al endpoint correspondiente.
    """
    group = Group.objects.create(name="Administrador")
    user = User.objects.create_user(username="admin_user", password="securepassword")
    user.groups.add(group)

    client = APIClient()
    client.login(username="admin_user", password="securepassword")

    response = client.get('/api/secretaria/')

    assert response.status_code == 403
    assert "detail" in response.data


@pytest.mark.django_db
def test_admin_access_allowed():
    """
    Verifica que un usuario en el grupo 'Administrador' tenga acceso al endpoint correspondiente.
    """
    group = Group.objects.create(name="Administrador")
    user = User.objects.create_user(username="admin_user", password="securepassword")
    user.groups.add(group)

    client = APIClient()
    client.login(username="admin_user", password="securepassword")

    response = client.get('/api/admin/')

    assert response.status_code == 200
    assert response.data.get("message") == "Acceso permitido a Administrador"
    assert response.data.get("user") == "admin_user"


@pytest.mark.django_db
def test_admin_access_denied():
    """
    Verifica que un usuario fuera del grupo 'Administrador' no tenga acceso al endpoint correspondiente.
    """
    group = Group.objects.create(name="Secretaria")
    user = User.objects.create_user(username="secretaria_user", password="securepassword")
    user.groups.add(group)

    client = APIClient()
    client.login(username="secretaria_user", password="securepassword")

    response = client.get('/api/admin/')

    assert response.status_code == 403
    assert "detail" in response.data
