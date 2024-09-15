#Uso de la libreria JSON para tratar tipo de dato JSON

import json

json_data='{"nombre":"Python","tipo":"Backend","paradigma":"POO"}'
print(json_data)
print(type(json_data))

json_to_python=json.loads(json_data)
print(json_to_python)
print(type(json_to_python))