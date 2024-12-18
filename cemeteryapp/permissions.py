from rest_framework.permissions import BasePermission, IsAdminUser

class IsInGroup(BasePermission):
    """
    Permiso para verificar si el usuario pertenece a un grupo específico.
    El grupo requerido se define en la vista utilizando 'required_group'.
    """
    def has_permission(self, request, view):
        required_group = getattr(view, 'required_group', None)
        if required_group is None:
            return False
        return request.user.groups.filter(name=required_group).exists()

class IsSuperUserOrAdmin(IsAdminUser):
    """
    Permiso para verificar si el usuario es superusuario o administrador.
    """
    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_superuser or request.user.is_staff))

class HasSpecificPermission(BasePermission):
    """
    Permiso para verificar si un usuario tiene un permiso específico.
    El permiso requerido se define en la vista utilizando 'required_permission'.
    """
    def has_permission(self, request, view):
        required_permission = getattr(view, 'required_permission', None)
        if required_permission is None:
            return False
        return request.user.has_perm(required_permission)