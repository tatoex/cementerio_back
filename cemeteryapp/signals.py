from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # crear grupos
    secretaria_group, _ = Group.objects.get_or_create(name='Secretaria')
    admin_group, _ = Group.objects.get_or_create(name='Administrador')

    # asignar permisos
        # difunto
    difunto_permissions = Permission.objects.filter(content_type__app_lable='difuntos')
    deudo_permissions = Permission.objects.filter(content_type__app_lable='deudos')
        # servicio
    servicio_permissions = Permission.objects.filter(content_type__app_lable='servicio')
        # iglesia
    iglesia_permissions = Permission.objects.filter(content_type__app_lable='iglesia')
    parroquia_permissions = Permission.objects.filter(content_type__app_lable='parroquia')
    link_red_social_permissions = Permission.objects.filter(content_type__app_lable='linkRedSocia')
        # articulo
    articulo_permissions = Permission.objects.filter(content_type__app_lable='articulo')
    guia_permissions = Permission.objects.filter(content_type__app_lable='guia')
    servicio_info_permissions = Permission.objects.filter(content_type__app_lable='servicio_info')
    seccion_articulo_permissions = Permission.objects.filter(content_type__app_lable='seccion_articulo')
        # obituario
    obituario_permissions = Permission.objects.filter(content_type__app_lable='obituario')
    memoria_permissions = Permission.objects.filter(content_type__app_lable='memoria')
    etapas_obituario_permissions = Permission.objects.filter(content_type__app_lable='etapas_obituario')

    secretaria_group.permissions.add(*difunto_permissions, *deudo_permissions)
    secretaria_group.permissions.add( *servicio_permissions)
    secretaria_group.permissions.add( *iglesia_permissions, *parroquia_permissions, *link_red_social_permissions)
    secretaria_group.permissions.add( *articulo_permissions, *guia_permissions, *servicio_info_permissions, *seccion_articulo_permissions)
    secretaria_group.permissions.add( *obituario_permissions, *memoria_permissions, *etapas_obituario_permissions)

    all_permissions=Permission.objects.all()
    admin_group.permissions.add(*all_permissions)
