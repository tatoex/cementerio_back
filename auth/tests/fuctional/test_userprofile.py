import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_retrieve_user_profile_success():
    """
    Verifica que un usuario autenticado pueda recuperar su perfil exitosamente.
    """
    _user = User.objects.create_user(  # Prefijo `_` para evitar advertencias
        username="test_user",
        password="securepassword",
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"
    )
    client = APIClient()
    client.login(username="test_user", password="securepassword")
    response = client.get('/api/userprofile/')
    assert response.status_code == 200
    assert response.data.get("username") == "test_user"
    assert response.data.get("first_name") == "John"
    assert response.data.get("last_name") == "Doe"
    assert response.data.get("email") == "john.doe@example.com"



@pytest.mark.django_db
def test_retrieve_user_profile_unauthenticated():
    """
    Verifica que un usuario no autenticado no pueda recuperar un perfil.
    """
    client = APIClient()
    response = client.get('/api/userprofile/')

    assert response.status_code == 401
    assert "detail" in response.data
    assert response.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_update_user_profile_success():
    """
    Verifica que un usuario autenticado pueda actualizar parcialmente su perfil.
    """
    _user = User.objects.create_user(  # Prefijo `_` para evitar advertencias
        username="test_user",
        password="securepassword",
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"
    )
    client = APIClient()
    client.login(username="test_user", password="securepassword")
    update_data = {
        "first_name": "Johnny",
        "last_name": "Doe",
        "email": "johnny.doe@example.com"
    }
    response = client.patch('/api/userprofile/', update_data, format="json")
    assert response.status_code == 200
    assert response.data.get("first_name") == "Johnny"
    assert response.data.get("last_name") == "Doe"
    assert response.data.get("email") == "johnny.doe@example.com"



@pytest.mark.django_db
def test_update_user_profile_unauthenticated():
    """
    Verifica que un usuario no autenticado no pueda actualizar su perfil.
    """
    update_data = {
        "first_name": "Johnny",
        "last_name": "Doe",
        "email": "johnny.doe@example.com"
    }

    client = APIClient()
    response = client.patch('/api/userprofile/', update_data, format="json")

    assert response.status_code == 401
    assert "detail" in response.data
    assert response.data["detail"] == "Authentication credentials were not provided."
