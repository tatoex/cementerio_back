from rest_framework import serializers
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, Lote
from servicio.models import Servicio
from obituarios.models import Obituario, Memoria, EtapasObituario
from informativos.models import Articulo, Guia, ServicioInfo, SeccionArticulo
from iglesias.models import Parroquia, Iglesia, LinkRedSocial

class HistoricalDifuntoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Difunto.history.model
        fields=['history_id','id','names','last_names','idNumber','description','requestNumber','history_date','history_type','history_user']

class HistoricalDeudoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Deudo.history.model
        fields=['history_id','id','names','last_names','idNumber','phoneNumber','email','address','description','history_date','history_type','history_user']

class HistoricalTumbaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Tumba.history.model
        fields=['history_id','id','nicheNumber','nicheType','description','history_date','history_type','history_user']

class HistoricalLoteSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Lote.history.model
        fields=['history_id','id','blockName','typeblock','numbersblock','filas','columnas','limite','description','history_date','history_type','history_user']

class HistoricalServicioSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Servicio.history.model
        fields=['history_id','id','ceremony','startDate','endDate','description','history_date','history_type','history_user']



class HistoricalObituarioSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Obituario.history.model
        fields=['history_id','id','obituary_detail','cementery','place','name','date','description','history_date','history_type','history_user']


class HistoricalMemoriaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Memoria.history.model
        fields=['history_id','id','names','relationship','text','image','date','description','history_date','history_type','history_user']


class HistoricalEtapasObituarioSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=EtapasObituario.history.model
        fields=['history_id','id','stage_ceremony','place','date','description','history_date','history_type','history_user']

class HistoricalArticuloSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Articulo.history.model
        fields=['history_id','id','references','external_source','publication_date','author','is_featured','category','title','description_short','image','description','history_date','history_type','history_user']

class HistoricalGuiaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Guia.history.model
        fields=['history_id','id','steps','aditional_resources','category','title','description_short','image','description','history_date','history_type','history_user']

class HistoricalServicioInfoSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=ServicioInfo.history.model
        fields=['history_id','id','features','exclusions','category','title','description_short','image','description','history_date','history_type','history_user']

class HistoricalSeccionArticuloSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=SeccionArticulo.history.model
        fields=['history_id','id','subtitle','content','description','history_date','history_type','history_user']

class HistoricalParroquiaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Parroquia.history.model
        fields=['history_id','id','name','churches_number','image','history_date','history_type','history_user']

class HistoricalIglesiaSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=Iglesia.history.model
        fields=['history_id','id','name','address','latitude','longitude','phone','email','schedule','priest','image','history_date','history_type','history_user']

class HistoricalLinkRedSocialSerializer(serializers.ModelSerializer):
    history_user=serializers.StringRelatedField()
    class Meta:
        model=LinkRedSocial.history.model
        fields=['history_id','id','stage_type','history_date','history_type','history_user']