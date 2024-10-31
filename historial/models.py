from django.db import models
from simple_history.utils import get_history_model_for_model
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, Lote
from servicio.models import Servicio
from obituarios.models import Obituario, Memoria, EtapasObituario
from informativos.models import Articulo, Guia, ServicioInfo, SeccionArticulo
from iglesias.models import Parroquia, Iglesia, LinkRedSocial

HistoricalDifunto = get_history_model_for_model(Difunto)
HistoricalDeudo = get_history_model_for_model(Deudo)
HistoricalTumba = get_history_model_for_model(Tumba)
HistoricalLote = get_history_model_for_model(Lote)
HistoricalServicio = get_history_model_for_model(Servicio)
HistoricalObituario = get_history_model_for_model(Obituario)
HistoricalMemoria = get_history_model_for_model(Memoria)
HistoricalEtapasObituario = get_history_model_for_model(EtapasObituario)
HistoricalArticulo = get_history_model_for_model(Articulo)
HistoricalGuia = get_history_model_for_model(Guia)
HistoricalServicioInfo = get_history_model_for_model(ServicioInfo)
HistoricalSeccionArticulo = get_history_model_for_model(SeccionArticulo)
HistoricalParroquia = get_history_model_for_model(Parroquia)
HistoricalIglesia = get_history_model_for_model(Iglesia)
HistoricalLinkRedSocial = get_history_model_for_model(LinkRedSocial)