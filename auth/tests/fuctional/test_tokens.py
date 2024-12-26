import pytest
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

# Prueba de autenticación y obtención de token
@pytest.mark.django_db
def test_token_obtain_success():
    """
    Verifica que un usuario existente pueda autenticarse y obtener un token de acceso.
    """
    # Crear un usuario de prueba
    user = User.objects.create_user(username="testuser", password="securepassword")
    Group.objects.create(name="TestGroup")
    user.groups.add(Group.objects.get(name="TestGroup"))

    client = APIClient()

    # Solicitar un token con credenciales correctas
    response = client.post('/api/token/', {"username": "testuser", "password": "securepassword"})

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
    assert response.data["roles"] == ["TestGroup"]

@pytest.mark.django_db
def test_token_obtain_failure():
    """
    Verifica que el sistema no entregue un token con credenciales incorrectas.
    """
    client = APIClient()

    # Solicitar un token con credenciales incorrectas
    response = client.post('/api/token/', {"username": "wronguser", "password": "wrongpassword"})

    assert response.status_code == 401
    assert "access" not in response.data
    assert "refresh" not in response.data

@pytest.mark.django_db
def test_token_payload_content():
    """
    Verifica que el payload del token incluya los datos personalizados (roles, nombres, etc.).
    """
    # Crear un usuario de prueba con datos adicionales
    user = User.objects.create_user(
        username="detaileduser",
        password="securepassword",
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"
    )
    group = Group.objects.create(name="TestGroup")
    user.groups.add(group)

    # Generar un token manualmente
    refresh = RefreshToken.for_user(user)
    payload = refresh.access_token.payload

    assert payload["roles"] == ["TestGroup"]
    assert payload["first_name"] == "John"
    assert payload["last_name"] == "Doe"
    assert payload["email"] == "john.doe@example.com"

@pytest.mark.django_db
def test_refresh_token():
    """
    Verifica que el refresh token permita obtener un nuevo token de acceso.
    """
    user = User.objects.create_user(username="testuser", password="securepassword")
    client = APIClient()

    # Solicitar tokens
    response = client.post('/api/token/', {"username": "testuser", "password": "securepassword"})
    refresh_token = response.data.get("refresh")

    # Solicitar un nuevo token de acceso con el refresh token
    response = client.post('/api/token/refresh/', {"refresh": refresh_token})

    assert response.status_code == 200
    assert "access" in response.data

@pytest.mark.django_db
def test_token_expired():
    """
    Verifica que el sistema detecte y rechace un token expirado (simulado).
    """
    user = User.objects.create_user(username="expireduser", password="securepassword")
    refresh = RefreshToken.for_user(user)

    # Simular expiración
    refresh.set_exp(lifetime=-1)  # Establecer un tiempo negativo para forzar la expiración

    client = APIClient()
    expired_token = str(refresh.access_token)

    # Usar el token expirado para realizar una solicitud
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {expired_token}")
    response = client.get('/api/some-protected-endpoint/')  # Reemplaza con una ruta protegida válida

    assert response.status_code == 401
    assert response.data.get("detail") == "Token is invalid or expired"
