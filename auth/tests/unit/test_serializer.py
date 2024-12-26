import pytest
from django.contrib.auth.models import User, Group
from auth.serializers import (
    CustomTokenObtainPairSerializer,
    UserProfileSerializer,
    GroupSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
def test_custom_token_obtain_pair_serializer():
    """
    Verifica que el CustomTokenObtainPairSerializer incluya roles, nombres y correo electrónico en el token.
    """
    group = Group.objects.create(name="Administrador")
    user = User.objects.create_user(
        username="testuser",
        password="testpassword",
        first_name="Test",
        last_name="User",
        email="testuser@example.com"
    )
    user.groups.add(group)

    token = RefreshToken.for_user(user)
    serializer = CustomTokenObtainPairSerializer.get_token(user)

    assert serializer["roles"] == ["Administrador"]
    assert serializer["first_name"] == "Test"
    assert serializer["last_name"] == "User"
    assert serializer["email"] == "testuser@example.com"


@pytest.mark.django_db
def test_user_profile_serializer():
    """
    Verifica que UserProfileSerializer serialice correctamente un usuario.
    """
    user = User.objects.create_user(
        username="testuser",
        password="testpassword",
        first_name="Test",
        last_name="User",
        email="testuser@example.com"
    )
    serializer = UserProfileSerializer(user)

    assert serializer.data["username"] == "testuser"
    assert serializer.data["first_name"] == "Test"
    assert serializer.data["last_name"] == "User"
    assert serializer.data["email"] == "testuser@example.com"


@pytest.mark.django_db
def test_group_serializer():
    """
    Verifica que GroupSerializer serialice correctamente un grupo.
    """
    group = Group.objects.create(name="Secretaria")
    serializer = GroupSerializer(group)

    assert serializer.data["id"] == group.id
    assert serializer.data["name"] == "Secretaria"
