def obtener_historial_limitado(model, object_id, limit=5):
    """
    Obtiene y devuelve las últimas 'limit' versiones del historial de un objeto dado su ID.
    - Lanza un error si hay menos de dos versiones.
    """
    historial = model.history.filter(id=object_id).order_by('-history_date')[:limit]
    if len(historial) < 2:
        raise ValueError("No hay suficientes versiones para comparar.")
    return historial

def compara_varias_versiones(model, object_id, attribute="all", limit=5):
    """
    Compara varias versiones consecutivas del historial de un objeto dado su ID.
    - Si 'attribute' es "all", compara todos los campos del objeto en cada versión.
    - Si se proporciona un 'attribute', solo compara ese atributo a lo largo de las versiones.
    """
    historial = obtener_historial_limitado(model, object_id, limit)
    cambios = []

    for i in range(len(historial) - 1):
        diferencias = historial[i].diff_against(historial[i + 1]).changes
        if attribute != "all":
            diferencias = [cambio for cambio in diferencias if cambio.field == attribute]
        if diferencias:
            cambios.append({
                "version_id": historial[i].history_id,
                "fecha": historial[i].history_date,
                "cambios": [
                    {"campo": cambio.field, "antes": cambio.old, "despues": cambio.new}
                    for cambio in diferencias
                ]
            })

    return cambios