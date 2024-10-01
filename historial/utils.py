def consultar_historial(model,object_id):
    """
    Consulta el historial completo de un objeto dado su ID
    """
    return model.history.filter(id=object_id).order_by('-history_date')

def obtener_historial_limitado(model, object_id, limit=5):
    """
    Obtiene y devuelve las ultimas 'limit' versiones del historial de un objeto.
    - lanza un error si hay menos de dos versiones.
    """
    historial=consultar_historial(model, object_id)[:limit]
    if len(historial)<2:
        raise ValueError(f"No hay suficientes versiones para comparar.")
    return historial

def comparar_versiones(version1, version2, attribute="all"):
    """
    Compara dos versiones consecutivas del historial:
    - Si 'attribute' es "all", compara todos los campos del objeto.
    - Si propocionas un 'attribute' solo comparara ese atributo.
    """
    diferencias=version1.diff_against(version2).changes
    # si el atributo es "all", no fitrara y devolvera todos los campos
    if attribute != "all":
        diferencias = [cambio for cambio in diferencias if cambio.field == attribute]
    return[
        {"campo": cambio.field,"antes":cambio.old, "despues":cambio.new}
        for cambio in diferencias
    ]
def compara_varias_versiones(model, object_id, attribute="all", limit=5):
    """
    Comparar varias versiones consecutivas del historial de un objeto.
    - Si 'attribute' es "all", compara todas las versiones.
    - Si propocionas un 'attribute' solo comparara ese atributo a lo largo de las versiones .
    """
    historial = obtener_historial_limitado(model, object_id, limit)
    cambios = []

    for i in range(len(historial)-1):

        diferencias = comparar_versiones(historial[i], historial[i+1], attribute)
        if diferencias:
            cambios.append({
                "version_id": historial[i].history_id,
                "fecha": historial[i].history_date,
                "cambios": diferencias
            })   
    return cambios