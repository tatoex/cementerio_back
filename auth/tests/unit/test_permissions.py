import pytest
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIRequestFactory
from cemeteryapp.permissions import IsInGroup
from django.contrib.auth.models import User, Group

@pytest.mark.django_db
def test_is_in_group_permission_granted():
    """
    Verifica que IsInGroup permita acceso a usuarios que pertenecen al grupo requerido.
    """
    factory = APIRequestFactory()
    request = factory.get("/dummy-url")

    # Crear usuario y grupo
    group = Group.objects.create(name="Secretaria")
    user = User.objects.create_user(username="testuser", password="testpassword")
    user.groups.add(group)
    request.user = user

    # Verificar permiso
    permission = IsInGroup()
    permission.required_group = "Secretaria"
    assert permission.has_permission(request, None) is True


@pytest.mark.django_db
def test_is_in_group_permission_denied():
    """
    Verifica que IsInGroup deniegue acceso a usuarios que no pertenecen al grupo requerido.
    """
    factory = APIRequestFactory()
    request = factory.get("/dummy-url")

    # Crear usuario sin grupo
    user = User.objects.create_user(username="testuser", password="testpassword")
    request.user = user

    # Verificar permiso
    permission = IsInGroup()
    permission.required_group = "Administrador"
    assert permission.has_permission(request, None) is False


@pytest.mark.django_db
def test_is_authenticated_permission_granted():
    """
    Verifica que IsAuthenticated permita acceso a usuarios autenticados.
    """
    factory = APIRequestFactory()
    request = factory.get("/dummy-url")

    # Crear usuario autenticado
    user = User.objects.create_user(username="testuser", password="testpassword")
    request.user = user

    # Verificar permiso
    permission = IsAuthenticated()
    assert permission.has_permission(request, None) is True


@pytest.mark.django_db
def test_is_authenticated_permission_denied():
    """
    Verifica que IsAuthenticated deniegue acceso a usuarios no autenticados.
    """
    factory = APIRequestFactory()
    request = factory.get("/dummy-url")

    # Usuario no autenticado
    request.user = None

    # Verificar permiso
    permission = IsAuthenticated()
    assert permission.has_permission(request, None) is False
