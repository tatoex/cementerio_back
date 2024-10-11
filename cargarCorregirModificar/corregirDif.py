import json
import random

# Path del archivo de entrada
input_file_path = '/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/difunto_data_final.json'

# Path del archivo de salida
output_file_path = '/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/difunto_data_finall.json'

# Cargar los datos desde el archivo JSON
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)

# Definir el rango máximo de tumbas
max_tumba_number = 6322

# Crear una lista de números disponibles entre 1 y el máximo, excluyendo los que ya existen
used_tumba_numbers = {entry['tumba'] for entry in data if entry['tumba'] is not None and entry['tumba'] <= max_tumba_number}
available_tumba_numbers = list(set(range(1, max_tumba_number + 1)) - used_tumba_numbers)

# Iterar sobre los datos y reemplazar los números de tumba mayores que 6322
for entry in data:
    if entry['tumba'] is not None and entry['tumba'] > max_tumba_number:
        # Seleccionar un número disponible aleatoriamente
        new_tumba_number = random.choice(available_tumba_numbers)
        entry['tumba'] = new_tumba_number
        # Remover el número asignado de la lista de disponibles
        available_tumba_numbers.remove(new_tumba_number)

# Guardar los datos actualizados en un nuevo archivo JSON
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=4)

print(f'Archivo actualizado guardado en: {output_file_path}')
