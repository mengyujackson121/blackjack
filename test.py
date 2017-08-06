import random
import json
from pprint import pprint

with open('conf.json') as data_file:
    data = json.load(data_file)
print(data["players"][0]["name"])


size = int(input("size?"))

lists = [[] for _ in range(size)]
while input("input C:") != 'q':
    for each in lists:
        each.append(random.randrange(1, 10))
    print(lists)
