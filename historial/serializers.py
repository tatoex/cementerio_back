from rest_framework import serializers
from .models import (HistoricalDifunto,
                     HistoricalDeudo,
                     HistoricalTumba,
                     HistoricalLote,
                     HistoricalServicio,
                     HistoricalObituario,
                     HistoricalMemoria,
                     HistoricalEtapasObituario,
                     HistoricalArticulo,
                     HistoricalGuia,
                     HistoricalServicioInfo,
                     HistoricalSeccionArticulo,
                     HistoricalParroquia,
                     HistoricalIglesia,
                     HistoricalLinkRedSocial)

class HistoricalDifuntoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=HistoricalDifunto
        fields='__all__'

class HistoricalDeudoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=HistoricalDeudo
        fields='__all__'

class HistoricalTumbaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=HistoricalTumba
        fields='__all__'

class HistoricalLoteSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=HistoricalLote
        fields='__all__'

class HistoricalServicioSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()

    class Meta:
        model = HistoricalServicio  # Cambia esto para usar el modelo histórico
        fields = '__all__'


class HistoricalObituarioSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalObituario
        fields='__all__'


class HistoricalMemoriaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalMemoria
        fields='__all__'

class HistoricalEtapasObituarioSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalEtapasObituario
        fields='__all__'

class HistoricalArticuloSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalArticulo
        fields='__all__'

class HistoricalGuiaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalGuia
        fields='__all__'

class HistoricalServicioInfoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalServicioInfo
        fields='__all__'

class HistoricalSeccionArticuloSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalSeccionArticulo
        fields='__all__'

class HistoricalParroquiaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalParroquia
        fields='__all__'

class HistoricalIglesiaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalIglesia
        fields='__all__'

class HistoricalLinkRedSocialSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model = HistoricalLinkRedSocial
        fields='__all__'