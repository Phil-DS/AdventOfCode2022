from data import data
from collections import defaultdict
from functools import cache
from queue import PriorityQueue

# data = '''#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#'''

# data = '''#.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#'''

split_data = data.splitlines()

width = len(split_data[0])
height = len(split_data)

blizzard_zero = set()
for y,row in enumerate(split_data):
    for x,cell in enumerate(row):
        if cell == '.':
            continue
        blizzard_zero.add((x,y,cell))

dirDict = {
    '<': (-1,0),
    '>': (1,0),
    '^': (0,-1),
    'v': (0,1)
}

@cache
def getBlizzardState(time):
    '''
    Get the blizzard at the current time. Due to the caching, it is memoized
    if time is 0: returns blizzard 0
    time: time you want.
    '''
    # if time == 0:
    #     return blizzard_zero

    
    nextBlizzard = set()

    for x,y,d in blizzard_zero:
            if d == '#':
                nextBlizzard.add((x,y))
                continue

            dx,dy = dirDict[d]
            nx = 1 + ((x+(dx*time)-1)%(width-2))
            ny = 1 + ((y+(dy*time)-1)%(height-2))

            # if nx == 0:
            #     nx = width - 2
            # if nx == (width-1):
            #     nx = 1
            # if ny == 0:
            #     ny = height - 2
            # if ny == (height-1):
            #     ny = 1

            nextBlizzard.add((nx,ny))

    return nextBlizzard

assert getBlizzardState(0) == getBlizzardState((width-2)*(height-2)), 'X'


_start = (1,0)
_end = (width - 2, height - 1)

# queue = PriorityQueue()
# queue.put_nowait((0,0,start))
def doTheBlizzardRun(start,end):
    queue = [(0,start)]

    tested = {(0,start)}

    while len(queue):
        time, coords = queue.pop(0)

        if coords == end:
            return time


        x,y = coords

        l = (x-1,y)
        r = (x+1,y)
        u = (x,y-1)
        d = (x,y+1)
        w = (x,y)

        nextBlizzardFrame = getBlizzardState(((time+1)%((width-2)*(height-2))))

        for p in [l,r,u,d,w]:
            if p[0] < 0 or p[1] < 0 or p[0] > (width-1) or p[1] > (height-1):
                continue
            
            if p in nextBlizzardFrame:
                continue
            
            if (time+1,p) in tested:
                continue

            queue.append((time+1,p))
            tested.add((time+1,p))

print(doTheBlizzardRun(_start,_end))