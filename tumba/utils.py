from django.utils import timezone

def actualizar_estado_disponibilidad(tumba):
    """
    Actualiza el estado 'available' de la tumba basando en la fecha actual y la fecha de DisponibilidadTumba
    """
    DisponibleTumba=models.get_model('tumba','DisponibleTumba')
    disponibilidad=DisponibleTumba.objects.filter(numberTumba=tumba).first()
    if disponibilidad:
        now=timezone.now()
        # verificando si la fecha actual esta dentro del rango de Disponibilidad
        if disponibilidad.startDate<=now<=disponibilidad.endDate:
            tumba.available=False
        else:
            tumba.available=True
        tumba.save()