from rest_framework import serializers
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, Lote, DisponibleTumba
from servicio.models import Servicio, Ceremonia

class HistoricalDifuntoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Difunto.history.model
        fields=['history_id','id','names','last_names','idNumber','decription','requestNumber','history_date','history_type','history_user']

class HistoricalDeudoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Deudo.history.model
        fields=['history_id','id','names','last_names','idNumber','phoneNumber','email','address','decription','history_date','history_type','history_user']

class HistoricalTumbaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Tumba.history.model
        fields=['history_id','id','nicheNumbe','nicheType','decription','history_date','history_type','history_user']

class HistoricalLoteSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Lote.history.model
        fields=['history_id','id','blockName','typeblock','numbersblock','filas','columnas','limite','decription','history_date','history_type','history_user']

class HistoricalDisponibleTumbaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=DisponibleTumba.history.model
        fields=['history_id','id','startDate','endDate','decription','history_date','history_type','history_user']

class HistoricalServicioSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Servicio.history.model
        fields=['history_id','id','startDate','endDate','decription','history_date','history_type','history_user']

class HistoricalCeremoniaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Ceremonia.history.model
        fields=['history_id','id','names','date','decription','history_date','history_type','history_user']

