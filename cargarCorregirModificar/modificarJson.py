import requests
import json

# Ruta del archivo JSON
json_file_path = "/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/deudo_converted.json"

# Leer el archivo JSON
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# URL base de la API
base_url = "http://127.0.0.1:8000/api/deudos/"

# Iterar sobre cada objeto JSON y actualizar en la base de datos
for index, data in enumerate(json_data):
    # Obtener el ID del lote desde el JSON
    lote_id = data.get("id")  # Utilizamos 'id' como el identificador del lote
    if lote_id is None:
        print(f"Error: El lote en el índice {index} no tiene un ID.")
        continue
    
    # Construir la URL de la API con el ID
    url = f"{base_url}{lote_id}/"
    
    # Realizar la solicitud PUT para actualizar el recurso
    response = requests.put(url, json=data)
    
    # Verificar el estado de la respuesta
    if response.status_code == 200:
        print(f"Lote {lote_id} actualizado correctamente.")
    else:
        print(f"Error al actualizar lote {lote_id}. Código de estado: {response.status_code}")
        print(f"Detalles del error: {response.json()}")
