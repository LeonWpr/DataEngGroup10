import json
import random

data = json.load(open("filepath.json"))
print(json.dumps(data, indent=4))

keys_to_be_deleted = [random.randint(0, len(data)-1) for _ in range(3)]
[data.pop(i) for i in keys_to_be_deleted]
print(json.dumps(data, indent=4))