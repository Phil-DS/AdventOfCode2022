from data import data

priority = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priorityScore = 0

for rucksack in data:
    size = len(rucksack) // 2
    lhs = set(rucksack[:size])
    rhs = set(rucksack[size:])
    u = lhs.intersection(rhs)

    for i in set(u):
        priorityScore += priority.index(i)

print(priorityScore)
