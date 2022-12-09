from data import data

position_set = set([(0, 0),])
head_position = (0, 0)
tail_position = (0, 0)

for d, l in data:
    for change in range(l):
        match d:
            case 'L':
                new_head_position = (head_position[0] - 1, head_position[1])
            case 'R':
                new_head_position = (head_position[0] + 1, head_position[1])
            case 'U':
                new_head_position = (head_position[0], head_position[1] + 1)
            case 'D':
                new_head_position = (head_position[0], head_position[1]-1)
        if abs(new_head_position[0] - tail_position[0]) > 1 or abs(new_head_position[1] - tail_position[1]) > 1:
            tail_position = head_position
            position_set.add(tail_position)
        head_position = new_head_position

print(len(position_set))
