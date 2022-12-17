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


area = []
jetDir = {
    '>': 1,
    '<': -1
}

maxY = -1

for i in range(2022):
    nextY = maxY + 4
    area.extend(0 for _ in range(8))
    # get rock
    # rock = next(rockCycle)
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

with open('day17/rock_out.txt','w') as f:
    for row in reversed(area):
        print(*['#' if a == '1' else '.' for a in bin(row)[2:].zfill(7)],sep='',file=f)
print(maxY+1)