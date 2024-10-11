import json

# Ruta del archivo JSON
json_file_path = "/home/renato/tesis/back/cementerio_back/lotes_custom_format.json"
output_file_path = "/home/renato/tesis/back/cementerio_back/lotes_corrected.json"

# Leer el archivo JSON
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Inicializar un contador para los IDs secuenciales
id_counter = 1

# Lista para almacenar los datos corregidos
corrected_data = []

# Iterar sobre cada objeto y asignar IDs únicos secuenciales
for item in json_data:
    item['id'] = id_counter  # Asignar el ID secuencial
    corrected_data.append(item)
    id_counter += 1  # Incrementar el contador

# Guardar el archivo corregido
with open(output_file_path, 'w') as outfile:
    json.dump(corrected_data, outfile, indent=4)

print(f"Archivo corregido guardado en: {output_file_path}")
