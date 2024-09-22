import json

data_python = {'nombre': 'Milagros', 'edad': 32, 'distrito': 'Jesús María'}

data_python_to_json = json.dumps(data_python)
print(data_python_to_json)
print(type(data_python_to_json))
