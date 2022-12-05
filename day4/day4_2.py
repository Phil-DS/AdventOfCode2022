from data import data

count = 0
for a, b in data:
    a_range = set(range(a[0], a[1]+1))
    b_range = set(range(b[0], b[1]+1))

    if a_range.intersection(b_range):
        count += 1
print(count)
