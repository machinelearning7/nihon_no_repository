import json

filename = 'numbers.json'
with open(filename) as f:
        numbers = json.load(f)

print(numbers)

#for this to work number_reader.py needs to be open first