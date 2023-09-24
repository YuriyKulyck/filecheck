import json

with open('data.json', 'r') as f:
    data = json.load(f)

data['age'] = 19
data['name'] = 'Lebron James'
data['occupation'] = 'Basketball'

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)