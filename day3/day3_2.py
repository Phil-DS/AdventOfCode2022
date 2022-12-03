from data import data

priority = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priorityScore = 0

for g in range(0,len(data),3):
    u = set(data[g]).intersection(data[g+1]).intersection(data[g+2])

    for i in set(u):
        priorityScore += priority.index(i)

print(priorityScore)
