from data import passMap, route
import re

dirMap = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

splitMap = passMap.splitlines()

height = len(splitMap)
width = max(map(len, splitMap))

pos = None
direction = 0

for x, cell in enumerate(splitMap[0]):
    if cell != ' ':
        pos = (x, 0)
        break

routeList = re.sub('([RL])', lambda x: f' {x.group(0)} ', route).split(' ')

wrapLookup = {
    (1,0,2): (0,2,0),
    (1,0,3): (0,3,0),
    (2,0,0): (1,2,2),
    (2,0,1): (1,1,2), 
    (2,0,3): (0,3,3),
    (1,1,0): (2,0,3),
    (1,1,2): (0,2,1),
    (0,2,2): (1,0,0),
    (0,2,3): (1,1,0),
    (1,2,0): (2,0,2),
    (1,2,1): (0,3,2),
    (0,3,0): (1,2,3),
    (0,3,1): (2,0,1),
    (0,3,2): (1,0,1)
  }

def wrap(p, d):
    x,y = p
    (qx,qy,nd) = wrapLookup[(x//50,y//50,d)]
    (dx,dy) = (x%50,y%50)
    i = [dy, 49-dx, 49-dy, dx][d]
    nx,ny = [(0,i),(49-i, 0),(49,49-i),(i,49)][nd]
    np = (qx*50 + nx, qy*50 + ny)
    print(p, np)
    return np, nd

for i,action in enumerate(routeList):
    match action:
        case 'L':
            direction = (direction+3) % 4
        case 'R':
            direction = (direction+5) % 4
        case _:
            distance = int(action)
            for d in range(distance):
                # get next known space
                lastPos = pos
                lastDir = direction
                
                pos = (pos[0]+dirMap[direction][0],pos[1]+dirMap[direction][1])
                try:
                    if pos[0] < 0 or pos[1] < 0 or splitMap[pos[1]][pos[0]] == ' ':
                        pos, direction = wrap(lastPos,lastDir)
                except:
                    pos, direction = wrap(lastPos,lastDir)
                if splitMap[pos[1]][pos[0]] == '#':
                    pos = lastPos
                    direction = lastDir
                    break

print(pos)
print(direction)
print(1000*(pos[1]+1)+4*(pos[0]+1)+direction)