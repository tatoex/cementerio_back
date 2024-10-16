from rest_framework import serializers
from .models import Parroquia, Iglesia, LinkRedSocial

class ParroquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquia
        fields = '__all__'

class IglesiaSerializer(serializers.ModelSerializer):
    # parish = ParroquiaSerializer(read_only=True)
    class Meta:
        model = Iglesia
        fields = '__all__'

class LinkRedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkRedSocial
        fields = '__all__'