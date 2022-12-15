from data import data

limits = (1000, 200)
init = (500,0)

field = [[0 for x in range(limits[0])] for y in range(limits[1])]

maxy = 0

for line in data:
    curr = None
    for point in line:
        if curr is not None:
            
            for _x in range(min(curr[0],point[0]),max(curr[0],point[0])+1):
                for _y in range(min(curr[1],point[1]),max(curr[1],point[1])+1):
                    field[_y][_x] = 1
        curr = point
        maxy = max(maxy,curr[1])

maxy += 2
for _x in range(limits[0]):
    field[maxy][_x] = 1

i = 0
while True:
    pos = init
    while True:
        x,y = pos
        if not field[y+1][x]:
            pos = (x,y+1)
            continue
        if not field[y+1][x-1]:
            pos = (x-1,y+1)
            continue
        if not field[y+1][x+1]:
            pos = (x+1,y+1)
            continue
        break
    field[pos[1]][pos[0]] = 2
    i+=1
    if field[init[1]][init[0]]:
        print(i)
        break