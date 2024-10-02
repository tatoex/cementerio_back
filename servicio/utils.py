
from tumba.models import DisponibleTumba

def sincronizar_disponibilidad_tumba(servicio):
    """Sincroniza las fechas de Disponibilidad en funcion a servicio"""
    if servicio.numberTomb is None:
        return
    dispobilidad=DisponibleTumba.objects.filter(numberTumba=servicio.numberTomb).first()
    if dispobilidad is None:
        return
    dispobilidad.startDate = servicio.startDate
    dispobilidad.endDate = servicio.endDate
    dispobilidad.save()