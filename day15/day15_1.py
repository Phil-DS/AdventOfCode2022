from data import data

filledPoints = set()
knownBeacons = set()
count = 0
checkVal = 2000000

for s,b in data:
    # filledPoints.add(s)
    # filledPoints.add(b)
    sx,sy = s
    bx,by = b
    if by == checkVal:
        knownBeacons.add(bx)
    max_distance = abs(sx-bx) + abs(sy-by)
    if abs(sy-checkVal)<=max_distance:
        diff = max_distance - abs(sy-checkVal)

        for dx in range(sx-diff, sx+diff+1):
            filledPoints.add(dx)
            
print(len(filledPoints - knownBeacons))