from functools import reduce
from data import data

width = len(data[0])
height = len(data)
count = 0
inner_found = []


def innerLoop(tree, x, y):
    ss = [0,0,0,0]
    for x2 in range(x-1, -1, -1):

        ss[0]+=1
        if data[y][x2] >= tree:
            break

    for y2 in range(y-1, -1, -1):

        ss[1] += 1
        if data[y2][x] >= tree:
            break

    for x2 in range(x+1, width):

        ss[2] += 1
        if data[y][x2] >= tree:
            break

    for y2 in range(y+1, height):

        ss[3] += 1
        if data[y2][x] >= tree:
            break
    return ss

best_ss = 0
best_ss_coord = None

for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width-1 or y == height -1:
            continue
        tree = data[y][x]
        sss = innerLoop(tree,x,y)
        ss = sss[0]*sss[1]*sss[2]*sss[3]
        if ss > best_ss:
            best_ss = ss
            best_ss_coord = (x,y)
            
print(best_ss)