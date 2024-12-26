import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group
from rest_framework import status

@pytest.mark.django_db
def test_secretaria_view_access_granted():
    """
    Verifica que los usuarios del grupo 'Secretaria' tengan acceso al endpoint.
    """
    client = APIClient()
    group = Group.objects.create(name="Secretaria")
    user = User.objects.create_user(username="secretaria_user", password="testpassword")
    user.groups.add(group)
    client.force_authenticate(user=user)

    response = client.get("/api/secretaria/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Acceso permitido a Secretaría"


@pytest.mark.django_db
def test_secretaria_view_access_denied():
    """
    Verifica que los usuarios fuera del grupo 'Secretaria' no tengan acceso al endpoint.
    """
    client = APIClient()
    user = User.objects.create_user(username="non_secretaria_user", password="testpassword")
    client.force_authenticate(user=user)

    response = client.get("/api/secretaria/")

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_admin_view_access_granted():
    """
    Verifica que los usuarios del grupo 'Administrador' tengan acceso al endpoint.
    """
    client = APIClient()
    group = Group.objects.create(name="Administrador")
    user = User.objects.create_user(username="admin_user", password="testpassword")
    user.groups.add(group)
    client.force_authenticate(user=user)

    response = client.get("/api/administrador/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Acceso permitido a Administrador"


@pytest.mark.django_db
def test_admin_view_access_denied():
    """
    Verifica que los usuarios fuera del grupo 'Administrador' no tengan acceso al endpoint.
    """
    client = APIClient()
    user = User.objects.create_user(username="non_admin_user", password="testpassword")
    client.force_authenticate(user=user)

    response = client.get("/api/administrador/")

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_user_profile_view_retrieve_authenticated_user():
    """
    Verifica que un usuario autenticado pueda obtener su propio perfil.
    """
    client = APIClient()
    user = User.objects.create_user(username="test_user", password="testpassword", first_name="John", last_name="Doe")
    client.force_authenticate(user=user)

    response = client.get(f"/api/userprofiles/{user.id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == "test_user"
    assert response.data["first_name"] == "John"
    assert response.data["last_name"] == "Doe"


@pytest.mark.django_db
def test_group_view_list_groups():
    """
    Verifica que se puedan listar todos los grupos disponibles.
    """
    client = APIClient()
    group1 = Group.objects.create(name="Secretaria")
    group2 = Group.objects.create(name="Administrador")

    response = client.get("/api/groups/")

    assert response.status_code == status.HTTP_200_OK
    assert any(group["name"] == group1.name for group in response.data)
    assert any(group["name"] == group2.name for group in response.data)


@pytest.mark.django_db
def test_group_view_retrieve_group_by_id():
    """
    Verifica que se pueda obtener un grupo por su ID.
    """
    client = APIClient()
    group = Group.objects.create(name="Secretaria")

    response = client.get(f"/api/groups/{group.id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Secretaria"
