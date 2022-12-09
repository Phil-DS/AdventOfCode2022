from data import data

width = len(data[0])
height = len(data)
count = 0
inner_found = []


def innerLoop(tree, x, y):
    flag = True
    for x2 in range(0, x):

        if data[y][x2] >= tree:
            flag = False
            break
    if flag:
        return True
    flag = True

    for y2 in range(0, y):

        if data[y2][x] >= tree:
            flag = False
            break
    if flag:
        return True
    flag = True

    for x2 in range(x+1, width):

        if data[y][x2] >= tree:
            flag = False
            break
    if flag:
        return True
    flag = True

    for y2 in range(y+1, height):

        if data[y2][x] >= tree:
            flag = False
            break
        
    return flag

for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width-1 or y == height -1:
            count += 1
            continue
        tree = data[y][x]
        if innerLoop(tree,x,y):#
            inner_found.append((x,y))
            count += 1
print(count)