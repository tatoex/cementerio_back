def consultar_historial(model,object_id):
    """consulta el historial completo de un objeto dado su ID"""
    return model.history.filter(id=object_id).order_by('-history_date')

# def obtener_historial_id(model. object_id):
#     """Devuelve el historial complet de un objeto con ID"""
#     historial=consultar_historial(model, object_id)
#     if not historial.exists():
#         raise ValueError(f"No se encontro historial para el objeto con id {object_id}")
#     return historial

def obtener_difernecia(version1, version2):
    """compara dos versiones del historial y devueve la diferencia"""
    diferencias=version1.diff_against(version2).changes
    return [
        {"campo": cambio.field,
        "antes": cambio.old,
        "despues": cambio.new}
        for cambio in diferencias  # Itera sobre 'changes' o la lista que tengas
    ]
def restaurar_version(version):
    """Restaura un objeto a una version anterior."""
    version.instance.save()