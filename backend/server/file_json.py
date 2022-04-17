import json

data = {}


with open('persons.json', 'w') as outfile:
    json.dumps(data, indent=4)