from data import data

limit = 4000000

filledPoints = set()
count = 0
max_distances = []
start = 0 # 3204480 # incase I fuck up and need to redo it.

for s,b in data:
    sx,sy = s
    bx,by = b
    max_distances.append(abs(sx-bx) + abs(sy-by))

for checkVal in range(start,limit):
    ranges = []
    for s,b in data:
        sx,sy = s
        bx,by = b
        max_distance = abs(sx-bx) + abs(sy-by)
        if abs(sy-checkVal)<=max_distance:
            diff = max_distance - abs(sy-checkVal)
            ranges.append((max(0,sx-diff),min(limit,sx+diff)))
    ranges.sort(key=lambda x:x[0])
    # print(ranges)
    init_range = ranges[0]
    for r in ranges[1:]:
        if r[1] < init_range[1]:
            continue
        if r[0] <=init_range[1]:
            init_range = (init_range[0],r[1])
            continue
        # we have a gap!
        # print((init_range[1],checkVal))
        print(((init_range[1]+1)*4000000)+checkVal)
        break
    # print(init_range)




            

# print(len(filledPoints))