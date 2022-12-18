from data import data

SA = 0

mask = [
    (1,0,0),
    (-1,0,0),
    (0,1,0),
    (0,-1,0),
    (0,0,1),
    (0,0,-1)
]

for x,y,z in data:
    SA += 6
    for dx,dy,dz in mask:
        if (x+dx,y+dy,z+dz) in data:
            SA -= 1

print(SA)