import json
from datetime import datetime

# Load the JSON data for servicio and tumba
servicio_data_path = '/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/updated_servicio_decimal.json'
tumba_data_path = '/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/updated_tumba_with_ids.json'

with open(servicio_data_path, 'r') as servicio_file:
    servicio_data = json.load(servicio_file)

with open(tumba_data_path, 'r') as tumba_file:
    tumba_data = json.load(tumba_file)

# Define the current date
current_date = datetime.now()

# Iterate over each servicio entry and update availability in tumba
for servicio in servicio_data:
    # Handle both formats: with and without milliseconds, and with 'Z' at the end
    start_date_str = servicio['startDate'].replace("Z", "")
    end_date_str = servicio['endDate'].replace("Z", "")
    
    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M:%S')
    
    try:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M:%S')
    
    # Determine if current date is within the range
    is_available = not (start_date <= current_date <= end_date)
    
    # Find the corresponding tumba by numberTomb (which now compares with id in tumba)
    for tumba in tumba_data:
        if tumba['id'] == servicio['numberTomb']:  # Comparing with the id attribute
            # Update the 'available' field
            tumba['available'] = is_available
            break  # Break after updating the corresponding tumba

# Save the updated tumba data to a new JSON file (all tumbas, not just updated ones)
output_file = '/home/renato/tesis/back/cementerio_back/cargarCorregirModificar/updated_tumba.json'
with open(output_file, 'w') as outfile:
    json.dump(tumba_data, outfile, indent=4)

print(f"Tumba actualizada guardada en: {output_file}")
