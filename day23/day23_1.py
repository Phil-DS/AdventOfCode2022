from collections import defaultdict
from data import data

rounds = 10

current = {*data}

offsets = [
    (-1,-1),
    (0,-1),
    (1,-1),
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0)
]

masks = [
    (0b00000111,(0,-1)),
    (0b01110000,(0,1)),
    (0b11000001,(-1,0)),
    (0b00011100,(1,0))
]

def getNeighborMask(pos):
    x,y = pos
    v = 0
    for i,d in enumerate(offsets):
        dx,dy = d
        if (x+dx,y+dy) in current:
            v |= 1 << i
    return v



for _ in range(rounds):
    newPos = defaultdict(list)
    # masks = map(getNeighborMask, current)
    for elf in current:
        nMask = getNeighborMask(elf)
        if nMask == 0:
            newPos[elf].append(elf)
            continue
        flag = False
        for mask,direction in masks:
            if nMask & mask == 0:
                newPos[(elf[0]+direction[0],elf[1]+direction[1])].append(elf)
                flag = True
                break
        if not flag:
            newPos[elf].append(elf)
    nextRound = set()
    for k,v in newPos.items():
        if len(v) == 1:
            nextRound.add(k)
        else:
            for p in v:
                nextRound.add(p)
    masks.append(masks.pop(0))
    current = nextRound
    # with open('test.txt','w') as f:
    #     for j in range(12):
    #         for i in range(14):
    #             c = '#' if (i,j) in current else '.'
    #             print(c,sep='',end='',file=f)
    #         print(file=f)


xs = list(map(lambda x: x[0], current))        
ys = list(map(lambda x: x[1], current))        

minX = min(xs)
maxX = max(xs)
miny = min(ys)
maxy = max(ys)
 

area = (1 + maxX - minX) * (1 + maxy - miny)
print(area - len(current))