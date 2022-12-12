import math
from data import data
from queue import PriorityQueue

maxx = len(data[0])
maxy = len(data)

inits = []

for i in range(maxy):
    for j in range(maxx):
        if data[i][j] == 'a' or data[i][j] == 'S':
            inits.append((j,i))
inits.sort(key=lambda x: math.sqrt(x[0]*x[0]+x[1]*x[1]))


best_route = math.inf

for init in inits:
    testQueue = PriorityQueue()
    testQueue.put((0,init))
    tested = set()

    while not testQueue.empty():
        weight, coords = testQueue.get_nowait()
        if weight > best_route:
            # break early, its not the best route
            break

        if coords in tested:
            continue

        tested.add(coords)
        # test surrounding
        x,y = coords
        currentElevation = data[y][x]

        if currentElevation == 'E':
            if weight < best_route:
                best_route = weight
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

        
print(best_route)