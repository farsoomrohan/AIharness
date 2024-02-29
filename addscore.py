import json

with open('hate_data.json', 'r') as file:
    data = json.load(file)

for item in data:
    item['score'] = 1  

with open('hate_data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Use indent for pretty-printing