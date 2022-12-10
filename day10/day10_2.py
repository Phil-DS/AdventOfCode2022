from data import data

x = 1
cycle = 1
vals = ['█']


for inst, val in data:
    match inst:
        case 'noop':
            cycle += 1
            vals.append('█' if abs(((cycle-1)%40) - x) <= 1 else '.')

        case 'addx':
            cycle += 1
            vals.append('█' if abs(((cycle-1)%40) - x) <= 1 else '.')
            cycle += 1
            x += val
            vals.append('█' if abs(((cycle-1)%40) - x) <= 1 else '.')

for i in range(0,220,40):
    print(*vals[i:i+40],sep='')
