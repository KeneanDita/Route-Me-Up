import json

person = {"name": "Alice", "age": 30, "city": "New York", "is_student": False}

serialized_person = json.dumps(person)
print(serialized_person)
print(type(serialized_person))
print(person)
print(type(person))
