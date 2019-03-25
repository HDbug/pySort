import json

with open('config.json') as config:
    setting = json.load(config)

with open('new.json', 'w') as f:
    json.dump(setting, f)