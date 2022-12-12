import math
from data import data
from queue import PriorityQueue

maxx = len(data[0])
maxy = len(data)


testQueue = PriorityQueue()

for i in range(maxy):
    for j in range(maxx):
        if data[i][j] == 'a' or data[i][j] == 'S':
            testQueue.put_nowait((0,(j,i)))

tested = set()

while not testQueue.empty():
    weight, coords = testQueue.get_nowait()
    if coords in tested:
        continue

    tested.add(coords)
    # test surrounding
    x,y = coords
    currentElevation = data[y][x]

    if currentElevation == 'E':
        print(weight)
        break

    if currentElevation == 'S':
        currentElevation = 'a'
    
    l = (x-1,y)
    r = (x+1,y)
    u = (x,y-1)
    d = (x,y+1)

    for n in [l,r,u,d]:
        if n in tested:
            continue
        nx,ny = n
        if nx < 0 or ny < 0 or nx >= maxx or ny >= maxy:
            continue

        newElevation = data[ny][nx]
        if newElevation == 'E':
            newElevation = 'z'

        if ord(newElevation) - ord(currentElevation) < 2:
            testQueue.put_nowait((weight+1,n))

