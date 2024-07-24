import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'data', 'data.json')
with open(file_path, 'r') as file:
    data = json.load(file)
print(data)