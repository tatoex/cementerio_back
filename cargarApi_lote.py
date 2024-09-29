import json
import requests

# URL de la API de tu aplicación
url = 'http://localhost:8000/api/lote/'  # Cambia esto a la URL correcta de tu API

# Ruta al archivo JSON
json_file_path = '/home/renato/tessis/djangorf/cementerio_back/lote.json'

# Leer el archivo JSON
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Hacer un POST a la API por cada registro, uno por uno
for item in data:
    response = requests.post(url, json=item)
    if response.status_code == 201:
        print(f'Registro agregado correctamente: {item}')
    else:
        print(f'Error al agregar registro: {item}')
        print(f'Error: {response.status_code}, {response.text}')