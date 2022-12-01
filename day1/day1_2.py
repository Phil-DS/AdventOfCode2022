from data import data

print(sum(list(sorted(sum(d) for d in data))[-3:]))