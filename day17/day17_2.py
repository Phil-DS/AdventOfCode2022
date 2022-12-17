from collections import defaultdict
from data import data
from itertools import cycle

rocks = [
    [(2,0),(3,0),(4,0),(5,0)],
    [(2,1),(3,1),(4,1),(3,0),(3,2)],
    [(2,0),(3,0),(4,0),(4,1),(4,2)],
    [(2,0),(2,1),(2,2),(2,3)],
    [(2,0),(2,1),(3,0),(3,1)]
]

# rockCycle = cycle(rocks)
# jetCycle = cycle(data)

rockCycle = cycle(range(len(rocks)))
jetCycle = cycle(range(len(data)))

max_rocks = 1000000000000

area = []
jetDir = {
    '>': 1,
    '<': -1
}

maxY = -1

seen = defaultdict(list)
heightMap = []
for i in range(4000):
    nextY = maxY + 4
    area.extend(0 for _ in range(8))
    # get rock
    rockID = next(rockCycle)
    rock = rocks[rockID]
    # set rock
    rock = [(x,y+nextY) for x,y in rock]
    #play rock
    # for jet in jetCycle:
    for jetId in jetCycle:
        jet = data[jetId]
        new_rock = [(x+jetDir[jet],y) for x,y in rock]
        if any((x < 0 or x > 6 or (area[y] & (1<<x))) for x,y in new_rock):
            new_rock = rock
        
        new_drop_rock = [(x,y-1) for x,y in new_rock]
        
        if any((y < 0 or (area[y] & (1<<x))) for x,y in new_drop_rock):
            for x,y in new_rock:
                if y > maxY:
                    maxY = y
                area[y] |= 1 << x
            break

        rock = new_drop_rock

    while area[-1] == 0:
        area.pop()


    if len(area) > 20:
        topState = tuple(area[-20:])
        key = (topState, jetId, rockID)
        seen[key].append((i, maxY))
        if len(seen[key]) > 1:
            r1, h1 = seen[key][-2]
            r2, h2 = seen[key][-1]
            if (max_rocks - r1) % (r2 - r1) == 0:
                result = (max_rocks - r1) // (r2 - r1) * (h2 - h1) + h1
                print(result)
                break

print(maxY + 1)

