import math
from data import data

position_set = set([(0, 0),])

positions = [(0,0) for _ in range(10)]

for d, l in data:
    for change in range(l):
        old_positions = list(positions)
        match d:
            case 'L':
                positions[0] = (positions[0][0] - 1, positions[0][1])
            case 'R':
                positions[0] = (positions[0][0] + 1, positions[0][1])
            case 'U':
                positions[0] = (positions[0][0], positions[0][1] + 1)
            case 'D':
                positions[0] = (positions[0][0], positions[0][1]-1)

        for i in range(1,10):
            dx = positions[i-1][0] - positions[i][0]
            dy = positions[i-1][1] - positions[i][1]
            if abs(dx) > 1 or abs(dy) > 1:
                positions[i] = (positions[i][0]+int(dx/(abs(dx) or 1)), positions[i][1]+int(dy/(abs(dy) or 1)))

        position_set.add(positions[-1])
print(len(position_set))

