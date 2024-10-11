import json

# Ruta del archivo JSON de entrada y salida
json_file_path = "/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/difunto_data_finall.json"
output_file_path = "/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/difunto_data_final.json"

# Leer el archivo JSON
with open(json_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Inicializar un contador para los IDs secuenciales
id_counter = 1

# Lista para almacenar los datos corregidos
corrected_data = []

# Iterar sobre cada objeto y asignar IDs únicos secuenciales
for item in json_data:
    item['id'] = id_counter  # Asignar el ID secuencial
    corrected_data.append(item)
    id_counter += 1  # Incrementar el contador para el próximo ID

# Guardar el archivo corregido
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(corrected_data, outfile, ensure_ascii=False, indent=4)

print(f"Archivo corregido guardado en: {output_file_path}")