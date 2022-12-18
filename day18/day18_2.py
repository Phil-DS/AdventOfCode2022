from data import data

mask = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

def calcSA(points):
    SA = 0

    for x, y, z in points:
        SA += 6
        for dx, dy, dz in mask:
            if (x+dx, y+dy, z+dz) in points:
                SA -= 1

    return SA


area = {(x, y, z) for x in range(22) for y in range(22) for z in range(22)}
empty_space = list(area - data)
air_pockets = []

while empty_space:
    to_check = [empty_space[0]]
    current_bubble = set()

    while len(to_check):
        next_air = to_check.pop()

        if next_air in empty_space:
            current_bubble.add(next_air)
            empty_space.remove(next_air)

            x, y, z = next_air
            for dx, dy, dz in mask:
                to_check.append((x+dx, y+dy, z+dz))

    if (0, 0, 0) not in current_bubble:
        air_pockets.append(current_bubble)

full_SA = calcSA(data)
air_pocket_SAs = [calcSA(pocket) for pocket in air_pockets]

print(full_SA - sum(air_pocket_SAs))
