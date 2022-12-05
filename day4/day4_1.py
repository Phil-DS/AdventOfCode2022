from data import data

count = 0
for a,b in data:
    if a[0] >= b[0] and a[1] <= b[1]:
        count += 1
        continue

    if b[0] >= a[0] and b[1] <= a[1]:
        count += 1
        continue
print(count)