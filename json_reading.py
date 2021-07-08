import json

with open('/Users/ilaydadastan/Downloads/accounts.json') as f:
  data = json.load(f)
  
""" In order to operate with the json file, the json file must be read first. """

print(data)
