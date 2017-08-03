import random


size = int(input("size?"))

lists = [[] for _ in range(size)]
while input("input C:") != 'q':
    for each in lists:
        each.append(random.randrange(1, 10))
    print(lists)
