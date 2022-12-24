from data import passMap, route
import re

dirMap = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

splitMap = passMap.splitlines()

height = len(splitMap)
width = max(map(len,splitMap))

pos = None
direction = 0

for x,cell in enumerate(splitMap[0]):
    if cell != ' ':
        pos = (x,0)
        break

routeList = re.sub('([RL])',lambda x: f' {x.group(0)} ',route).split(' ')

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
                while True:
                    try:
                        pos = ((pos[0]+dirMap[direction][0]+width)%width,(pos[1]+dirMap[direction][1]+height)%height)
                        if splitMap[pos[1]][pos[0]] != ' ':
                            break
                    except:
                        pass
                if splitMap[pos[1]][pos[0]] == '#':
                    pos = lastPos
                    break

print(pos)
print(direction)
print(1000*(pos[1]+1)+4*(pos[0]+1)+direction)