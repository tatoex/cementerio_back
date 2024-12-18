from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Agregar datos adicionales al token (esto irá en el payload del token)
        data['roles'] = [group.name for group in self.user.groups.all()]
        data['first_name'] = self.user.first_name or ''  # Agregar primer nombre
        data['last_name'] = self.user.last_name or ''    # Agregar apellido
        data['email'] = self.user.email or ''           # Agregar email

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar datos personalizados al payload del token
        token['roles'] = [group.name for group in user.groups.all()]
        token['first_name'] = user.first_name or ''
        token['last_name'] = user.last_name or ''
        token['email'] = user.email or ''

        return token


class UserProfileSerializer(serializers.ModelSerializer): # Aquí se debe especificar many=True si es necesario
    class Meta:
        model = User
        fields = '__all__'  # O especifica los campos que necesites

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']  # Campos expuestos

