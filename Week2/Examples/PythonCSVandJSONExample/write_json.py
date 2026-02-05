import json

person = {
  'name': 'Alice',
  'age': 30,
  'city': 'New York'
}

with open('person.json', 'w') as f:
  json.dump(person, f)